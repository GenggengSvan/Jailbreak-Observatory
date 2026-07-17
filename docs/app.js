(() => {
  "use strict";

  const data = window.OBSERVATORY_DATA;
  if (!data || !Array.isArray(data.papers)) {
    document.body.innerHTML = '<p style="padding:2rem">The Observatory dataset could not be loaded.</p>';
    return;
  }

  const NS = "http://www.w3.org/2000/svg";
  const CATEGORY_COLORS = {
    Attack: "#ff6b5f",
    Defense: "#56d6a4",
    Benchmark: "#f0c75e",
    Mechanism: "#70a9ff",
    Other: "#bd95ee",
  };
  const CATEGORIES = Object.keys(CATEGORY_COLORS);
  const NODE_W = 230;
  const NODE_H = 74;
  const NODE_GAP = 18;
  const COLS = 3;
  const YEAR_WIDTH = 790;
  const TOP_GUTTER = 150;
  const papers = data.papers;
  const relations = data.relations || [];
  const paperById = new Map(papers.map((paper) => [paper.id, paper]));
  const positions = new Map();
  const relationsById = new Map(papers.map((paper) => [paper.id, []]));
  relations.forEach((relation) => {
    relationsById.get(relation.source)?.push(relation);
    relationsById.get(relation.target)?.push(relation);
  });

  const svg = document.getElementById("map");
  const viewport = document.getElementById("viewport");
  const timelineLayer = document.getElementById("timelineLayer");
  const edgeLayer = document.getElementById("edgeLayer");
  const nodeLayer = document.getElementById("nodeLayer");
  const searchInput = document.getElementById("searchInput");
  const detailPanel = document.getElementById("detailPanel");
  const state = {
    selected: null,
    activeCategories: new Set(CATEGORIES),
    query: "",
    scale: 1,
    tx: 0,
    ty: 0,
    dragging: false,
    moved: false,
    pointerX: 0,
    pointerY: 0,
  };

  let graphWidth = 1000;
  let graphHeight = 800;
  let toastTimer = null;

  const el = (name, attributes = {}, text = "") => {
    const node = document.createElementNS(NS, name);
    Object.entries(attributes).forEach(([key, value]) => node.setAttribute(key, value));
    if (text) node.textContent = text;
    return node;
  };

  const shortenVenue = (venue) => {
    const aliases = {
      "International Conference on Learning Representations": "ICLR",
      "Annual Meeting of the Association for Computational Linguistics": "ACL",
      "Conference on Empirical Methods in Natural Language Processing": "EMNLP",
      "USENIX Security Symposium": "USENIX",
      "IEEE Symposium on Security and Privacy": "S&P",
    };
    return aliases[venue] || venue;
  };

  const wrapTitle = (title, limit = 30, lines = 3) => {
    const words = title.split(/\s+/);
    const output = [];
    let current = "";
    for (const word of words) {
      const candidate = current ? `${current} ${word}` : word;
      if (candidate.length > limit && current) {
        output.push(current);
        current = word;
        if (output.length === lines - 1) break;
      } else {
        current = candidate;
      }
    }
    if (output.length < lines && current) output.push(current);
    const consumed = output.join(" ").length;
    if (consumed < title.length - 1) output[output.length - 1] = output[output.length - 1].replace(/[.,:;]?$/, "…");
    return output.slice(0, lines);
  };

  const isPaperVisible = (paper) => {
    if (!state.activeCategories.has(paper.category)) return false;
    if (!state.query) return true;
    const haystack = `${paper.title} ${paper.venue} ${paper.category} ${paper.target} ${paper.year} ${paper.status || ""}`.toLowerCase();
    return haystack.includes(state.query);
  };

  function buildLayout() {
    const years = [...new Set(papers.map((paper) => paper.year))].sort((a, b) => a - b);
    const byYearCategory = new Map();
    years.forEach((year) => CATEGORIES.forEach((category) => byYearCategory.set(`${year}:${category}`, [])));
    papers.forEach((paper) => {
      const key = `${paper.year}:${CATEGORIES.includes(paper.category) ? paper.category : "Other"}`;
      byYearCategory.get(key)?.push(paper);
    });
    byYearCategory.forEach((group) => group.sort((a, b) => (b.citations || 0) - (a.citations || 0) || a.title.localeCompare(b.title)));

    const bandHeights = new Map();
    CATEGORIES.forEach((category) => {
      const rows = Math.max(...years.map((year) => Math.ceil(byYearCategory.get(`${year}:${category}`).length / COLS)), 1);
      bandHeights.set(category, Math.max(260, 116 + rows * (NODE_H + NODE_GAP)));
    });

    let bandY = TOP_GUTTER;
    const bandStarts = new Map();
    CATEGORIES.forEach((category) => {
      bandStarts.set(category, bandY);
      bandY += bandHeights.get(category);
    });
    graphWidth = years.length * YEAR_WIDTH + 180;
    graphHeight = bandY + 90;

    CATEGORIES.forEach((category) => {
      const y = bandStarts.get(category);
      timelineLayer.append(el("line", { x1: 90, y1: y, x2: graphWidth - 70, y2: y, class: "lane-line" }));
      timelineLayer.append(el("text", {
        x: 92, y: y + 27, class: "lane-label", fill: CATEGORY_COLORS[category],
      }, category));
    });

    years.forEach((year, yearIndex) => {
      const yearX = 150 + yearIndex * YEAR_WIDTH;
      const count = papers.filter((paper) => paper.year === year).length;
      timelineLayer.append(el("line", { x1: yearX - 34, y1: 70, x2: yearX - 34, y2: graphHeight - 70, class: "year-line" }));
      timelineLayer.append(el("text", { x: yearX, y: 85, class: "year-label" }, String(year)));
      timelineLayer.append(el("text", { x: yearX + 3, y: 107, class: "year-count" }, `${count} PAPERS`));

      CATEGORIES.forEach((category) => {
        const group = byYearCategory.get(`${year}:${category}`);
        const startY = bandStarts.get(category) + 58;
        group.forEach((paper, index) => {
          positions.set(paper.id, {
            x: yearX + (index % COLS) * (NODE_W + NODE_GAP),
            y: startY + Math.floor(index / COLS) * (NODE_H + NODE_GAP),
          });
        });
      });
    });
  }

  function buildDefs() {
    const defs = el("defs");
    const filter = el("filter", { id: "softGlow", x: "-40%", y: "-40%", width: "180%", height: "180%" });
    filter.append(el("feGaussianBlur", { stdDeviation: "5", result: "blur" }));
    const merge = el("feMerge");
    merge.append(el("feMergeNode", { in: "blur" }));
    merge.append(el("feMergeNode", { in: "SourceGraphic" }));
    filter.append(merge);
    defs.append(filter);
    svg.insertBefore(defs, viewport);
  }

  function edgePath(source, target) {
    const sx = source.x + NODE_W / 2;
    const sy = source.y + NODE_H / 2;
    const tx = target.x + NODE_W / 2;
    const ty = target.y + NODE_H / 2;
    const dx = Math.abs(tx - sx);
    const curve = Math.max(70, dx * 0.42);
    if (tx >= sx) return `M ${sx} ${sy} C ${sx + curve} ${sy}, ${tx - curve} ${ty}, ${tx} ${ty}`;
    return `M ${sx} ${sy} C ${sx - curve} ${sy}, ${tx + curve} ${ty}, ${tx} ${ty}`;
  }

  function renderEdges() {
    relations.forEach((relation, index) => {
      const source = positions.get(relation.source);
      const target = positions.get(relation.target);
      if (!source || !target) return;
      const path = el("path", {
        d: edgePath(source, target),
        class: `relation-edge ${relation.kind}`,
        "data-source": relation.source,
        "data-target": relation.target,
        "data-index": index,
      });
      edgeLayer.append(path);
    });
  }

  function renderNodes() {
    papers.forEach((paper) => {
      const position = positions.get(paper.id);
      if (!position) return;
      const color = CATEGORY_COLORS[paper.category] || CATEGORY_COLORS.Other;
      const group = el("g", {
        class: "paper-node",
        transform: `translate(${position.x} ${position.y})`,
        "data-id": paper.id,
        tabindex: "0",
        role: "button",
        "aria-label": `${paper.title}, ${shortenVenue(paper.venue)} ${paper.year}`,
        style: `--node-color:${color}`,
      });
      group.append(el("rect", { class: "node-card", x: 0, y: 0, width: NODE_W, height: NODE_H, rx: 3 }));
      group.append(el("rect", { class: "node-accent", x: 0, y: 0, width: 3, height: NODE_H, rx: 1.5 }));
      group.append(el("text", { class: "node-meta", x: 13, y: 17 }, `${shortenVenue(paper.venue)} · ${paper.year} · ${paper.target}`.toUpperCase()));
      const title = el("text", { class: "node-title", x: 13, y: 37 });
      wrapTitle(paper.title).forEach((line, index) => title.append(el("tspan", { x: 13, dy: index ? 14 : 0 }, line)));
      group.append(title);
      if (paper.citations !== null && paper.citations !== undefined) {
        group.append(el("text", { class: "node-citations", x: NODE_W - 12, y: 17, "text-anchor": "end" }, `${paper.citations} CITES`));
      }
      group.append(el("title", {}, paper.title));
      group.addEventListener("click", (event) => {
        event.stopPropagation();
        if (!state.moved) selectPaper(paper.id, true);
      });
      group.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          selectPaper(paper.id, true);
        }
      });
      nodeLayer.append(group);
    });
  }

  function updateVisibility() {
    const selectedRelations = state.selected ? relationsById.get(state.selected) || [] : [];
    const relatedIds = new Set();
    selectedRelations.forEach((relation) => {
      relatedIds.add(relation.source);
      relatedIds.add(relation.target);
    });

    nodeLayer.querySelectorAll(".paper-node").forEach((node) => {
      const id = node.dataset.id;
      const paper = paperById.get(id);
      const visible = isPaperVisible(paper);
      node.classList.toggle("hidden", !visible);
      node.classList.toggle("selected", id === state.selected);
      node.classList.toggle("related", state.selected && relatedIds.has(id) && id !== state.selected);
      node.classList.toggle("dimmed", Boolean(state.selected && !relatedIds.has(id)));
    });

    edgeLayer.querySelectorAll(".relation-edge").forEach((edge) => {
      const visible = Boolean(
        state.selected &&
        (edge.dataset.source === state.selected || edge.dataset.target === state.selected) &&
        isPaperVisible(paperById.get(edge.dataset.source)) &&
        isPaperVisible(paperById.get(edge.dataset.target))
      );
      edge.classList.toggle("visible", visible);
    });
  }

  function openDetails(paper) {
    const color = CATEGORY_COLORS[paper.category] || CATEGORY_COLORS.Other;
    detailPanel.style.setProperty("--panel-color", color);
    document.getElementById("panelKicker").textContent = `${paper.category} / ${paper.target}`;
    document.getElementById("panelTitle").textContent = paper.title;
    const meta = [shortenVenue(paper.venue), paper.year, paper.status, paper.citations !== null && paper.citations !== undefined ? `${paper.citations} citations` : null].filter(Boolean);
    document.getElementById("panelMeta").innerHTML = meta.map((item) => `<span>${escapeHtml(String(item))}</span>`).join("");
    const abstract = paper.abstract || "This entry comes from the conference index. Open the paper for its abstract, method, and evaluation details.";
    document.getElementById("panelAbstract").textContent = abstract.length > 920 ? `${abstract.slice(0, 917).trim()}…` : abstract;
    const count = (relationsById.get(paper.id) || []).length;
    document.getElementById("relationCount").textContent = `${count} research neighbors`;
    const links = [];
    if (paper.url) links.push(`<a href="${escapeAttribute(paper.url)}" target="_blank" rel="noreferrer">Open paper ↗</a>`);
    if (paper.codeUrl) links.push(`<a href="${escapeAttribute(paper.codeUrl)}" target="_blank" rel="noreferrer">Code ↗</a>`);
    links.push(`<a href="https://github.com/GenggengSvan/Jailbreak-Observatory/blob/master/${escapeAttribute(paper.source)}" target="_blank" rel="noreferrer">Source entry ↗</a>`);
    document.getElementById("panelLinks").innerHTML = links.join("");
    detailPanel.classList.add("open");
    detailPanel.setAttribute("aria-hidden", "false");
  }

  const escapeHtml = (value) => value.replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" })[char]);
  const escapeAttribute = escapeHtml;

  function closeDetails() {
    detailPanel.classList.remove("open");
    detailPanel.setAttribute("aria-hidden", "true");
  }

  function selectPaper(id, fit = false) {
    state.selected = id;
    updateVisibility();
    const paper = paperById.get(id);
    if (paper) openDetails(paper);
    if (fit) fitSelection(id);
  }

  function clearSelection() {
    state.selected = null;
    closeDetails();
    updateVisibility();
  }

  function applyTransform() {
    viewport.setAttribute("transform", `translate(${state.tx} ${state.ty}) scale(${state.scale})`);
  }

  function setScale(nextScale, centerX, centerY) {
    const rect = svg.getBoundingClientRect();
    const cx = centerX ?? rect.width / 2;
    const cy = centerY ?? rect.height / 2;
    const graphX = (cx - state.tx) / state.scale;
    const graphY = (cy - state.ty) / state.scale;
    state.scale = Math.max(0.055, Math.min(2.4, nextScale));
    state.tx = cx - graphX * state.scale;
    state.ty = cy - graphY * state.scale;
    applyTransform();
  }

  function fitBounds(bounds, maxScale = 1.05) {
    const rect = svg.getBoundingClientRect();
    const padding = Math.min(100, rect.width * 0.08);
    const width = Math.max(1, bounds.maxX - bounds.minX);
    const height = Math.max(1, bounds.maxY - bounds.minY);
    state.scale = Math.max(0.055, Math.min(maxScale, (rect.width - padding * 2) / width, (rect.height - padding * 2) / height));
    state.tx = rect.width / 2 - ((bounds.minX + bounds.maxX) / 2) * state.scale;
    state.ty = rect.height / 2 - ((bounds.minY + bounds.maxY) / 2) * state.scale;
    applyTransform();
  }

  function fitAll() {
    fitBounds({ minX: 55, minY: 35, maxX: graphWidth, maxY: graphHeight }, 0.75);
  }

  function fitYear(year) {
    const visible = papers.filter((paper) => paper.year === year).map((paper) => positions.get(paper.id)).filter(Boolean);
    if (!visible.length) return fitAll();
    fitBounds({
      minX: Math.min(...visible.map((position) => position.x)) - 85,
      minY: 45,
      maxX: Math.max(...visible.map((position) => position.x)) + NODE_W + 85,
      maxY: Math.max(...visible.map((position) => position.y)) + NODE_H + 85,
    }, 0.82);
  }

  function fitSelection(id) {
    const position = positions.get(id);
    if (!position) return;
    const rect = svg.getBoundingClientRect();
    const panelWidth = window.innerWidth > 700 ? Math.min(440, window.innerWidth * 0.35) : 0;
    const availableWidth = Math.max(320, rect.width - panelWidth);
    state.scale = window.innerWidth > 700 ? 0.82 : 0.68;
    state.tx = availableWidth * 0.46 - (position.x + NODE_W / 2) * state.scale;
    state.ty = rect.height * 0.48 - (position.y + NODE_H / 2) * state.scale;
    applyTransform();
  }

  function fitVisibleSearch() {
    const visible = papers.filter(isPaperVisible).map((paper) => positions.get(paper.id)).filter(Boolean);
    if (!visible.length) {
      showToast("No papers match this search and filter combination.");
      return;
    }
    fitBounds({
      minX: Math.min(...visible.map((position) => position.x)) - 60,
      minY: Math.min(...visible.map((position) => position.y)) - 60,
      maxX: Math.max(...visible.map((position) => position.x)) + NODE_W + 60,
      maxY: Math.max(...visible.map((position) => position.y)) + NODE_H + 60,
    }, visible.length === 1 ? 1.25 : 0.85);
  }

  function createFilters() {
    const container = document.getElementById("categoryFilters");
    CATEGORIES.forEach((category) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "filter-chip active";
      button.textContent = category;
      button.style.setProperty("--chip-color", CATEGORY_COLORS[category]);
      button.addEventListener("click", () => {
        if (state.activeCategories.has(category)) state.activeCategories.delete(category);
        else state.activeCategories.add(category);
        if (!state.activeCategories.size) CATEGORIES.forEach((item) => state.activeCategories.add(item));
        container.querySelectorAll(".filter-chip").forEach((chip) => chip.classList.toggle("active", state.activeCategories.has(chip.textContent)));
        if (state.selected && !isPaperVisible(paperById.get(state.selected))) clearSelection();
        updateVisibility();
        fitVisibleSearch();
      });
      container.append(button);
    });
  }

  function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("show"), 4200);
  }

  function wireInteractions() {
    svg.addEventListener("pointerdown", (event) => {
      if (event.target.closest?.(".paper-node")) return;
      state.dragging = true;
      state.moved = false;
      state.pointerX = event.clientX;
      state.pointerY = event.clientY;
      svg.classList.add("dragging");
      svg.setPointerCapture(event.pointerId);
    });
    svg.addEventListener("pointermove", (event) => {
      if (!state.dragging) return;
      const dx = event.clientX - state.pointerX;
      const dy = event.clientY - state.pointerY;
      if (Math.abs(dx) + Math.abs(dy) > 2) state.moved = true;
      state.tx += dx;
      state.ty += dy;
      state.pointerX = event.clientX;
      state.pointerY = event.clientY;
      applyTransform();
    });
    const stopDrag = () => {
      state.dragging = false;
      svg.classList.remove("dragging");
      setTimeout(() => { state.moved = false; }, 0);
    };
    svg.addEventListener("pointerup", stopDrag);
    svg.addEventListener("pointercancel", stopDrag);
    svg.addEventListener("click", (event) => {
      if (!event.target.closest?.(".paper-node") && !state.moved) clearSelection();
    });
    svg.addEventListener("wheel", (event) => {
      event.preventDefault();
      const rect = svg.getBoundingClientRect();
      setScale(state.scale * Math.exp(-event.deltaY * 0.0012), event.clientX - rect.left, event.clientY - rect.top);
    }, { passive: false });

    document.getElementById("zoomInButton").addEventListener("click", () => setScale(state.scale * 1.28));
    document.getElementById("zoomOutButton").addEventListener("click", () => setScale(state.scale / 1.28));
    document.getElementById("resetButton").addEventListener("click", () => { clearSelection(); fitAll(); });
    document.getElementById("panelClose").addEventListener("click", clearSelection);

    let searchTimer;
    searchInput.addEventListener("input", () => {
      state.query = searchInput.value.trim().toLowerCase();
      clearTimeout(searchTimer);
      if (state.selected && !isPaperVisible(paperById.get(state.selected))) clearSelection();
      updateVisibility();
      searchTimer = setTimeout(fitVisibleSearch, 180);
    });

    const dialog = document.getElementById("aboutDialog");
    document.getElementById("aboutButton").addEventListener("click", () => dialog.showModal());
    dialog.querySelector(".dialog-close").addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });
    document.getElementById("legendInfo").addEventListener("click", () => showToast("Links are computed from shared category, target, year, venue, and title vocabulary. They are reading suggestions—not claims of citation or direct influence."));

    window.addEventListener("keydown", (event) => {
      if (event.key === "/" && document.activeElement !== searchInput) {
        event.preventDefault();
        searchInput.focus();
      }
      if (event.key === "Escape" && !dialog.open) clearSelection();
    });
    window.addEventListener("resize", () => { if (state.selected) fitSelection(state.selected); else fitAll(); });
  }

  function initialize() {
    buildDefs();
    buildLayout();
    renderEdges();
    renderNodes();
    createFilters();
    wireInteractions();
    document.getElementById("paperCount").textContent = papers.length;
    document.getElementById("venueCount").textContent = new Set(papers.map((paper) => shortenVenue(paper.venue))).size;
    document.getElementById("yearCount").textContent = new Set(papers.map((paper) => paper.year)).size;
    updateVisibility();
    const latestYear = Math.max(...papers.map((paper) => paper.year));
    requestAnimationFrame(() => fitYear(latestYear));
  }

  initialize();
})();
