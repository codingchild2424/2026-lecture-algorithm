/* ======================================================================
   Shortest Path Explorer -- Frontend Logic
   ====================================================================== */

document.addEventListener("DOMContentLoaded", () => {

    // -----------------------------------------------------------------
    // Tab switching
    // -----------------------------------------------------------------
    const tabBtns = document.querySelectorAll(".tab-btn");
    const panels  = document.querySelectorAll(".tab-panel");

    tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            tabBtns.forEach(b => b.classList.remove("active"));
            panels.forEach(p => p.classList.remove("active"));
            btn.classList.add("active");
            document.getElementById(btn.dataset.tab).classList.add("active");
        });
    });

    // -----------------------------------------------------------------
    // Helper: POST JSON to API
    // -----------------------------------------------------------------
    async function apiPost(url, body) {
        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body),
        });
        return res.json();
    }

    // -----------------------------------------------------------------
    // Helper: parse weighted edge list from text
    // Formats: "A-B:4", "A->B:4", "A B 4", "A-B" (default weight 1)
    // -----------------------------------------------------------------
    function parseWeightedEdges(text) {
        const edges = [];
        const parts = text.split(/[,\n]+/).map(s => s.trim()).filter(Boolean);
        for (const part of parts) {
            // Try "u-v:w" or "u->v:w"
            let m = part.match(/^(\S+?)\s*[->\s]+\s*(\S+?)\s*:\s*(-?[\d.]+)\s*$/);
            if (m) {
                edges.push([m[1], m[2], parseFloat(m[3])]);
                continue;
            }
            // Try "u-v w" or "u->v w"
            m = part.match(/^(\S+?)\s*[->\s]+\s*(\S+?)\s+(-?[\d.]+)\s*$/);
            if (m) {
                edges.push([m[1], m[2], parseFloat(m[3])]);
                continue;
            }
            // Try "u-v" (default weight 1)
            m = part.match(/^(\S+?)\s*[->\s]+\s*(\S+)$/);
            if (m) {
                edges.push([m[1], m[2], 1]);
            }
        }
        return edges;
    }

    function parseNodeList(text) {
        return text.split(/[\s,]+/).map(s => s.trim()).filter(Boolean);
    }

    // =================================================================
    // SVG Graph Rendering (weighted)
    // =================================================================

    const NS = "http://www.w3.org/2000/svg";
    const NODE_R = 22;

    /**
     * Render a weighted graph to an SVG element.
     *
     * @param {SVGElement} svg        - target SVG
     * @param {object}     graphData  - {nodes, edges: [{from, to, weight}], directed}
     * @param {object}     positions  - {nodeName: {x, y}}
     * @param {object}     opts       - highlight configuration
     *   opts.visitedNodes   - Set of visited node names
     *   opts.currentNode    - name of currently processed node
     *   opts.pathNodes      - Set of nodes on a shortest path
     *   opts.pathEdges      - Set of "u->v" strings for path edges
     *   opts.treeEdges      - Set of "u->v" strings for SPT edges
     *   opts.relaxedEdges   - Set of "u->v" strings for just-relaxed edges
     *   opts.negcycleEdges  - Set of "u->v" strings for negative cycle edges
     *   opts.negcycleNodes  - Set of node names in negative cycle
     *   opts.nodeClasses    - Map of nodeName -> extra CSS class
     *   opts.distMap        - Map of nodeName -> distance value (shown as badge)
     */
    function renderGraph(svg, graphData, positions, opts = {}) {
        svg.innerHTML = "";

        const directed = graphData.directed;

        // Arrowhead markers for directed edges
        if (directed) {
            const defs = document.createElementNS(NS, "defs");

            function makeMarker(id, color) {
                const marker = document.createElementNS(NS, "marker");
                marker.setAttribute("id", id);
                marker.setAttribute("viewBox", "0 0 10 10");
                marker.setAttribute("refX", "10");
                marker.setAttribute("refY", "5");
                marker.setAttribute("markerWidth", "8");
                marker.setAttribute("markerHeight", "8");
                marker.setAttribute("orient", "auto-start-reverse");
                const path = document.createElementNS(NS, "path");
                path.setAttribute("d", "M 0 0 L 10 5 L 0 10 z");
                path.setAttribute("fill", color);
                marker.appendChild(path);
                defs.appendChild(marker);
            }

            makeMarker("arrow-default", "#94a3b8");
            makeMarker("arrow-highlight", "#10b981");
            makeMarker("arrow-tree", "#818cf8");
            makeMarker("arrow-relaxed", "#f59e0b");
            makeMarker("arrow-negcycle", "#ef4444");
            svg.appendChild(defs);
        }

        const treeEdgeSet    = opts.treeEdges    || new Set();
        const pathEdgeSet    = opts.pathEdges     || new Set();
        const relaxedEdgeSet = opts.relaxedEdges  || new Set();
        const negcycleEdgeSet = opts.negcycleEdges || new Set();

        // Draw edges
        for (const edge of graphData.edges) {
            const u = edge.from;
            const v = edge.to;
            const w = edge.weight;
            const pu = positions[u];
            const pv = positions[v];
            if (!pu || !pv) continue;

            const dx = pv.x - pu.x;
            const dy = pv.y - pu.y;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const offset = directed ? NODE_R + 10 : NODE_R + 2;
            const ux = pu.x + (dx / dist) * (NODE_R + 2);
            const uy = pu.y + (dy / dist) * (NODE_R + 2);
            const vx = pv.x - (dx / dist) * offset;
            const vy = pv.y - (dy / dist) * offset;

            const line = document.createElementNS(NS, "line");
            line.setAttribute("x1", ux);
            line.setAttribute("y1", uy);
            line.setAttribute("x2", vx);
            line.setAttribute("y2", vy);

            let cls = "graph-edge";
            let markerEnd = directed ? "url(#arrow-default)" : "";

            const edgeKey = `${u}->${v}`;
            const edgeKeyRev = `${v}->${u}`;

            if (pathEdgeSet.has(edgeKey) || pathEdgeSet.has(edgeKeyRev)) {
                cls += " highlighted";
                markerEnd = directed ? "url(#arrow-highlight)" : "";
            } else if (negcycleEdgeSet.has(edgeKey) || negcycleEdgeSet.has(edgeKeyRev)) {
                cls += " negcycle-edge";
                markerEnd = directed ? "url(#arrow-negcycle)" : "";
            } else if (relaxedEdgeSet.has(edgeKey) || relaxedEdgeSet.has(edgeKeyRev)) {
                cls += " relaxed-edge";
                markerEnd = directed ? "url(#arrow-relaxed)" : "";
            } else if (treeEdgeSet.has(edgeKey) || treeEdgeSet.has(edgeKeyRev)) {
                cls += " tree-edge";
                markerEnd = directed ? "url(#arrow-tree)" : "";
            }

            line.setAttribute("class", cls);
            if (markerEnd) line.setAttribute("marker-end", markerEnd);
            svg.appendChild(line);

            // Weight label
            const mx = (pu.x + pv.x) / 2;
            const my = (pu.y + pv.y) / 2;
            // Offset the label slightly perpendicular to the edge
            const perpX = -dy / dist * 12;
            const perpY = dx / dist * 12;

            const bgRect = document.createElementNS(NS, "rect");
            const labelX = mx + perpX;
            const labelY = my + perpY;
            bgRect.setAttribute("x", labelX - 10);
            bgRect.setAttribute("y", labelY - 8);
            bgRect.setAttribute("width", 20);
            bgRect.setAttribute("height", 16);
            bgRect.setAttribute("rx", 3);
            bgRect.setAttribute("class", "edge-weight-bg");
            svg.appendChild(bgRect);

            const wLabel = document.createElementNS(NS, "text");
            wLabel.setAttribute("x", labelX);
            wLabel.setAttribute("y", labelY);
            wLabel.setAttribute("class", "edge-weight");
            wLabel.textContent = String(w);
            svg.appendChild(wLabel);
        }

        // Draw nodes
        const visitedSet    = opts.visitedNodes   || new Set();
        const pathNodeSet   = opts.pathNodes      || new Set();
        const negcycleNodeSet = opts.negcycleNodes || new Set();
        const nodeClasses   = opts.nodeClasses    || {};
        const distMap       = opts.distMap        || {};

        for (const nodeName of graphData.nodes) {
            const pos = positions[nodeName];
            if (!pos) continue;

            const g = document.createElementNS(NS, "g");
            let cls = "graph-node";

            if (nodeClasses[nodeName]) {
                cls += " " + nodeClasses[nodeName];
            } else if (nodeName === opts.currentNode) {
                cls += " current";
            } else if (pathNodeSet.has(nodeName)) {
                cls += " path-node";
            } else if (negcycleNodeSet.has(nodeName)) {
                cls += " negcycle-node";
            } else if (visitedSet.has(nodeName)) {
                cls += " visited";
            }

            g.setAttribute("class", cls);

            const circle = document.createElementNS(NS, "circle");
            circle.setAttribute("cx", pos.x);
            circle.setAttribute("cy", pos.y);
            circle.setAttribute("r", nodeName === opts.currentNode ? 25 : NODE_R);
            g.appendChild(circle);

            const text = document.createElementNS(NS, "text");
            text.setAttribute("x", pos.x);
            text.setAttribute("y", pos.y);
            text.textContent = nodeName;
            g.appendChild(text);

            svg.appendChild(g);

            // Distance badge
            if (distMap[nodeName] !== undefined) {
                const bx = pos.x + 18;
                const by = pos.y - 18;
                const bg = document.createElementNS(NS, "circle");
                bg.setAttribute("cx", bx);
                bg.setAttribute("cy", by);
                bg.setAttribute("r", 11);
                bg.setAttribute("class", "node-dist-bg");
                svg.appendChild(bg);

                const bt = document.createElementNS(NS, "text");
                bt.setAttribute("x", bx);
                bt.setAttribute("y", by);
                bt.setAttribute("class", "node-dist-badge");
                const dv = distMap[nodeName];
                bt.textContent = dv === "inf" ? "\u221E" : String(dv);
                svg.appendChild(bt);
            }
        }
    }


    // =================================================================
    // Helper: format distance table as text
    // =================================================================
    function formatDistTable(distances, source) {
        let lines = [`Source: ${source}\n`];
        lines.push("Node       Distance");
        lines.push("------     --------");
        const nodes = Object.keys(distances).sort();
        for (const n of nodes) {
            const d = distances[n];
            const dStr = d === "inf" ? "\u221E (unreachable)" : String(d);
            const marker = n === source ? " (source)" : "";
            lines.push(`${n.padEnd(10)} ${dStr}${marker}`);
        }
        return lines.join("\n");
    }


    // =================================================================
    // 1. DIJKSTRA'S ALGORITHM
    // =================================================================

    const dijDirected = document.getElementById("dij-directed");
    const dijNodes    = document.getElementById("dij-nodes");
    const dijEdges    = document.getElementById("dij-edges");
    const dijBuild    = document.getElementById("dij-build");
    const dijPreset   = document.getElementById("dij-preset");
    const dijSource   = document.getElementById("dij-source");
    const dijRun      = document.getElementById("dij-run");
    const dijStepBack = document.getElementById("dij-step-back");
    const dijStepFwd  = document.getElementById("dij-step-fwd");
    const dijPlay     = document.getElementById("dij-play");
    const dijStepInfo = document.getElementById("dij-step-info");
    const dijSvg      = document.getElementById("dij-svg");
    const dijDistTable = document.getElementById("dij-dist-table");
    const dijLog      = document.getElementById("dij-log");

    let dijGraphData = null;
    let dijPositions = null;
    let dijResult = null;
    let dijStepIdx = -1;
    let dijPlayTimer = null;

    // Build graph from inputs
    dijBuild.addEventListener("click", async () => {
        const nodes = parseNodeList(dijNodes.value);
        const edges = parseWeightedEdges(dijEdges.value);
        const directed = dijDirected.value === "true";
        const data = await apiPost("/api/graph/init", { directed, nodes, edges });
        dijGraphData = data.graph;
        dijPositions = data.positions;
        dijResult = null;
        dijStepIdx = -1;
        resetDijControls();
        renderGraph(dijSvg, dijGraphData, dijPositions);
        dijDistTable.textContent = "";
        dijLog.textContent = "";
    });

    // Load preset
    dijPreset.addEventListener("click", async () => {
        const data = await apiPost("/api/graph/preset", {});
        dijGraphData = data.graph;
        dijPositions = data.positions;
        dijResult = null;
        dijStepIdx = -1;
        resetDijControls();
        renderGraph(dijSvg, dijGraphData, dijPositions);
        dijDirected.value = String(data.graph.directed);
        dijNodes.value = data.graph.nodes.join(", ");
        dijEdges.value = data.graph.edges.map(e => `${e.from}-${e.to}:${e.weight}`).join(", ");
        dijDistTable.textContent = "";
        dijLog.textContent = "";
    });

    // Run Dijkstra
    dijRun.addEventListener("click", async () => {
        if (!dijGraphData) { alert("Build or load a graph first."); return; }
        const source = dijSource.value.trim() || dijGraphData.nodes[0] || "";
        const data = await apiPost("/api/dijkstra", { algorithm: "dijkstra", source });
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }
        dijGraphData = data.graph;
        dijPositions = data.positions;
        dijResult = data.result;
        dijStepIdx = -1;
        enableDijControls();
        renderGraph(dijSvg, dijGraphData, dijPositions);

        // Show final distance table
        dijDistTable.textContent = formatDistTable(dijResult.distances, dijResult.source) +
            `\n\nTotal relaxations: ${dijResult.relaxation_count}` +
            `\nExecution time: ${dijResult.time_ms} ms`;

        // Log
        let logText = "";
        dijResult.steps.forEach((s, i) => {
            logText += `Step ${i + 1}: Extract min => ${s.node} (dist=${s.distance})\n`;
            logText += `  Priority queue: [${s.priority_queue.map(pq => `(${pq[0]},${pq[1]})`).join(", ")}]\n`;
            if (s.relaxations.length > 0) {
                s.relaxations.forEach(r => {
                    const status = r.relaxed ? "RELAXED" : "no change";
                    logText += `  Edge ${r.edge} (w=${r.weight}): ${r.old_dist} -> ${r.new_dist} [${status}]\n`;
                });
            } else {
                logText += "  No neighbors to relax\n";
            }
            logText += "\n";
        });
        dijLog.textContent = logText;
    });

    function resetDijControls() {
        dijStepBack.disabled = true;
        dijStepFwd.disabled = true;
        dijPlay.disabled = true;
        dijStepInfo.textContent = "";
        clearInterval(dijPlayTimer);
        dijPlayTimer = null;
    }

    function enableDijControls() {
        dijStepFwd.disabled = false;
        dijPlay.disabled = false;
        dijStepBack.disabled = true;
        dijStepInfo.textContent = "Step 0 / " + dijResult.steps.length;
    }

    function renderDijStep() {
        if (!dijResult) return;
        const steps = dijResult.steps;
        const visited = new Set();
        const distMap = {};
        let current = null;
        const treeEdges = new Set();
        const relaxedEdges = new Set();

        for (let i = 0; i <= dijStepIdx && i < steps.length; i++) {
            visited.add(steps[i].node);
        }

        // Build tree edges from visited nodes
        for (const te of dijResult.tree_edges) {
            if (visited.has(te.to) || visited.has(te.from)) {
                treeEdges.add(`${te.from}->${te.to}`);
            }
        }

        if (dijStepIdx >= 0 && dijStepIdx < steps.length) {
            current = steps[dijStepIdx].node;
            // Show relaxations for the current step
            steps[dijStepIdx].relaxations.forEach(r => {
                if (r.relaxed) {
                    const parts = r.edge.split(" -> ");
                    relaxedEdges.add(`${parts[0]}->${parts[1]}`);
                }
            });
        }

        // Build distance map from current state
        // Start with infinity, apply step snapshots
        for (const n of dijGraphData.nodes) {
            distMap[n] = "inf";
        }
        if (dijResult.source) distMap[dijResult.source] = 0;
        for (let i = 0; i <= dijStepIdx && i < steps.length; i++) {
            distMap[steps[i].node] = steps[i].distance;
            steps[i].relaxations.forEach(r => {
                if (r.relaxed) {
                    const parts = r.edge.split(" -> ");
                    distMap[parts[1]] = r.new_dist;
                }
            });
        }

        const nodeClasses = {};
        nodeClasses[dijResult.source] = "source-node";

        renderGraph(dijSvg, dijGraphData, dijPositions, {
            visitedNodes: visited,
            currentNode: current,
            treeEdges,
            relaxedEdges,
            nodeClasses,
            distMap,
        });

        dijStepBack.disabled = dijStepIdx < 0;
        dijStepFwd.disabled = dijStepIdx >= steps.length - 1;
        dijStepInfo.textContent = `Step ${dijStepIdx + 1} / ${steps.length}`;
    }

    dijStepFwd.addEventListener("click", () => {
        if (!dijResult) return;
        if (dijStepIdx < dijResult.steps.length - 1) {
            dijStepIdx++;
            renderDijStep();
        }
    });

    dijStepBack.addEventListener("click", () => {
        if (!dijResult) return;
        if (dijStepIdx >= 0) {
            dijStepIdx--;
            if (dijStepIdx < 0) {
                renderGraph(dijSvg, dijGraphData, dijPositions);
                dijStepInfo.textContent = "Step 0 / " + dijResult.steps.length;
                dijStepBack.disabled = true;
                dijStepFwd.disabled = false;
            } else {
                renderDijStep();
            }
        }
    });

    dijPlay.addEventListener("click", () => {
        if (!dijResult) return;
        if (dijPlayTimer) {
            clearInterval(dijPlayTimer);
            dijPlayTimer = null;
            dijPlay.textContent = "Play";
            return;
        }
        dijPlay.textContent = "Pause";
        if (dijStepIdx >= dijResult.steps.length - 1) {
            dijStepIdx = -1;
            renderGraph(dijSvg, dijGraphData, dijPositions);
        }
        dijPlayTimer = setInterval(() => {
            if (dijStepIdx < dijResult.steps.length - 1) {
                dijStepIdx++;
                renderDijStep();
            } else {
                clearInterval(dijPlayTimer);
                dijPlayTimer = null;
                dijPlay.textContent = "Play";
            }
        }, 1000);
    });

    // Auto-load preset
    dijPreset.click();


    // =================================================================
    // 2. BELLMAN-FORD ALGORITHM
    // =================================================================

    const bfSource      = document.getElementById("bf-source");
    const bfRun         = document.getElementById("bf-run");
    const bfPresetNeg   = document.getElementById("bf-preset-neg");
    const bfPresetNegC  = document.getElementById("bf-preset-negcycle");
    const bfStepBack    = document.getElementById("bf-step-back");
    const bfStepFwd     = document.getElementById("bf-step-fwd");
    const bfPlay        = document.getElementById("bf-play");
    const bfStepInfo    = document.getElementById("bf-step-info");
    const bfSvg         = document.getElementById("bf-svg");
    const bfNegAlert    = document.getElementById("bf-negcycle-alert");
    const bfNegInfo     = document.getElementById("bf-negcycle-info");
    const bfDistTable   = document.getElementById("bf-dist-table");
    const bfLog         = document.getElementById("bf-log");

    let bfGraphData = null;
    let bfPositions = null;
    let bfResult = null;
    let bfStepIdx = -1;
    let bfPlayTimer = null;

    // Load preset with negative weights (no cycle)
    bfPresetNeg.addEventListener("click", async () => {
        const data = await apiPost("/api/graph/preset-negative", {});
        bfGraphData = data.graph;
        bfPositions = data.positions;
        bfResult = null;
        bfStepIdx = -1;
        resetBfControls();
        renderGraph(bfSvg, bfGraphData, bfPositions);
        bfDistTable.textContent = "";
        bfLog.textContent = "";
        bfNegAlert.style.display = "none";
        // Also update the main graph for comparison tab
        dijGraphData = data.graph;
        dijPositions = data.positions;
    });

    // Load preset with negative cycle
    bfPresetNegC.addEventListener("click", async () => {
        const data = await apiPost("/api/graph/preset-negcycle", {});
        bfGraphData = data.graph;
        bfPositions = data.positions;
        bfResult = null;
        bfStepIdx = -1;
        resetBfControls();
        renderGraph(bfSvg, bfGraphData, bfPositions);
        bfDistTable.textContent = "";
        bfLog.textContent = "";
        bfNegAlert.style.display = "none";
        dijGraphData = data.graph;
        dijPositions = data.positions;
    });

    // Run Bellman-Ford
    bfRun.addEventListener("click", async () => {
        if (!dijGraphData && !bfGraphData) {
            alert("Build or load a graph first (Dijkstra tab or use preset buttons here).");
            return;
        }
        // If we have a BF-specific graph (from presets), use it; otherwise use dijkstra tab graph
        const graphAvailable = bfGraphData || dijGraphData;
        const source = bfSource.value.trim() || graphAvailable.nodes[0] || "";
        const data = await apiPost("/api/bellman-ford", { algorithm: "bellman-ford", source });
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }
        bfGraphData = data.graph;
        bfPositions = data.positions;
        bfResult = data.result;
        bfStepIdx = -1;
        enableBfControls();
        renderGraph(bfSvg, bfGraphData, bfPositions);

        // Negative cycle alert
        if (bfResult.negative_cycle) {
            bfNegAlert.style.display = "block";
            const cycleEdgesStr = bfResult.negative_cycle_edges
                .map(e => `${e.from} -> ${e.to} (w=${e.weight})`)
                .join("\n");
            bfNegInfo.textContent =
                "A negative-weight cycle was detected!\n" +
                "Edges involved:\n" + cycleEdgesStr +
                "\n\nDistances below may not be meaningful for nodes reachable from the negative cycle.";
        } else {
            bfNegAlert.style.display = "none";
        }

        // Distance table
        bfDistTable.textContent = formatDistTable(bfResult.distances, bfResult.source) +
            `\n\nTotal relaxations: ${bfResult.relaxation_count}` +
            `\nIterations: ${bfResult.steps.length}` +
            `\nNegative cycle: ${bfResult.negative_cycle ? "YES" : "No"}` +
            `\nExecution time: ${bfResult.time_ms} ms`;

        // Log
        let logText = "";
        bfResult.steps.forEach((s) => {
            logText += `=== Iteration ${s.iteration} ===\n`;
            const relaxed = s.relaxations.filter(r => r.relaxed);
            if (relaxed.length > 0) {
                relaxed.forEach(r => {
                    logText += `  Edge ${r.edge} (w=${r.weight}): ${r.old_dist} -> ${r.new_dist} [RELAXED]\n`;
                });
            } else {
                logText += "  No edges relaxed\n";
            }
            logText += `  Distances: ${Object.entries(s.distances).map(([n,d]) => `${n}=${d}`).join(", ")}\n`;
            if (!s.any_relaxed) {
                logText += "  Early termination: no relaxation occurred\n";
            }
            logText += "\n";
        });
        bfLog.textContent = logText;
    });

    function resetBfControls() {
        bfStepBack.disabled = true;
        bfStepFwd.disabled = true;
        bfPlay.disabled = true;
        bfStepInfo.textContent = "";
        clearInterval(bfPlayTimer);
        bfPlayTimer = null;
    }

    function enableBfControls() {
        bfStepFwd.disabled = false;
        bfPlay.disabled = false;
        bfStepBack.disabled = true;
        bfStepInfo.textContent = "Iteration 0 / " + bfResult.steps.length;
    }

    function renderBfStep() {
        if (!bfResult) return;
        const steps = bfResult.steps;
        const distMap = {};
        const relaxedEdges = new Set();
        const treeEdges = new Set();
        const negcycleEdges = new Set();
        const negcycleNodes = new Set();

        // Initialize distances
        for (const n of bfGraphData.nodes) {
            distMap[n] = "inf";
        }
        distMap[bfResult.source] = 0;

        // Apply iterations up to current step
        for (let i = 0; i <= bfStepIdx && i < steps.length; i++) {
            const iter = steps[i];
            for (const [n, d] of Object.entries(iter.distances)) {
                distMap[n] = d;
            }
        }

        // Show relaxed edges for current iteration
        if (bfStepIdx >= 0 && bfStepIdx < steps.length) {
            steps[bfStepIdx].relaxations.forEach(r => {
                if (r.relaxed) {
                    const parts = r.edge.split(" -> ");
                    relaxedEdges.add(`${parts[0]}->${parts[1]}`);
                }
            });
        }

        // Tree edges from parent
        for (const te of bfResult.tree_edges) {
            treeEdges.add(`${te.from}->${te.to}`);
        }

        // Negative cycle
        if (bfResult.negative_cycle && bfStepIdx >= steps.length - 1) {
            bfResult.negative_cycle_edges.forEach(e => {
                negcycleEdges.add(`${e.from}->${e.to}`);
                negcycleNodes.add(e.from);
                negcycleNodes.add(e.to);
            });
        }

        const nodeClasses = {};
        nodeClasses[bfResult.source] = "source-node";

        renderGraph(bfSvg, bfGraphData, bfPositions, {
            treeEdges,
            relaxedEdges,
            negcycleEdges,
            negcycleNodes,
            nodeClasses,
            distMap,
        });

        bfStepBack.disabled = bfStepIdx < 0;
        bfStepFwd.disabled = bfStepIdx >= steps.length - 1;
        bfStepInfo.textContent = `Iteration ${bfStepIdx + 1} / ${steps.length}`;
    }

    bfStepFwd.addEventListener("click", () => {
        if (!bfResult) return;
        if (bfStepIdx < bfResult.steps.length - 1) {
            bfStepIdx++;
            renderBfStep();
        }
    });

    bfStepBack.addEventListener("click", () => {
        if (!bfResult) return;
        if (bfStepIdx >= 0) {
            bfStepIdx--;
            if (bfStepIdx < 0) {
                renderGraph(bfSvg, bfGraphData, bfPositions);
                bfStepInfo.textContent = "Iteration 0 / " + bfResult.steps.length;
                bfStepBack.disabled = true;
                bfStepFwd.disabled = false;
            } else {
                renderBfStep();
            }
        }
    });

    bfPlay.addEventListener("click", () => {
        if (!bfResult) return;
        if (bfPlayTimer) {
            clearInterval(bfPlayTimer);
            bfPlayTimer = null;
            bfPlay.textContent = "Play";
            return;
        }
        bfPlay.textContent = "Pause";
        if (bfStepIdx >= bfResult.steps.length - 1) {
            bfStepIdx = -1;
            renderGraph(bfSvg, bfGraphData, bfPositions);
        }
        bfPlayTimer = setInterval(() => {
            if (bfStepIdx < bfResult.steps.length - 1) {
                bfStepIdx++;
                renderBfStep();
            } else {
                clearInterval(bfPlayTimer);
                bfPlayTimer = null;
                bfPlay.textContent = "Play";
            }
        }, 1200);
    });


    // =================================================================
    // 3. ALGORITHM COMPARISON
    // =================================================================

    const cmpSource   = document.getElementById("cmp-source");
    const cmpRun      = document.getElementById("cmp-run");
    const cmpStats    = document.getElementById("cmp-stats");
    const cmpTableWrap = document.getElementById("cmp-table-wrap");
    const cmpDijDist  = document.getElementById("cmp-dij-dist");
    const cmpBfDist   = document.getElementById("cmp-bf-dist");
    const cmpDijSvg   = document.getElementById("cmp-dij-svg");
    const cmpBfSvg    = document.getElementById("cmp-bf-svg");

    cmpRun.addEventListener("click", async () => {
        if (!dijGraphData) {
            alert("Build or load a graph in the Dijkstra tab first.");
            return;
        }
        const source = cmpSource.value.trim() || dijGraphData.nodes[0] || "";
        const data = await apiPost("/api/compare", { source });
        if (data.error) {
            alert(data.error);
            return;
        }

        const dijk = data.dijkstra;
        const bf = data.bellman_ford;

        // Stats boxes
        cmpStats.innerHTML = `
            <div class="stat-box">
                <div class="stat-value">${source}</div>
                <div class="stat-label">Source Node</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">${data.graph.nodes.length}</div>
                <div class="stat-label">Nodes</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">${data.graph.edges.length}</div>
                <div class="stat-label">Edges</div>
            </div>
        `;

        // Comparison table
        const dijRelax = dijk.relaxation_count;
        const bfRelax = bf.relaxation_count;
        const dijTime = dijk.time_ms;
        const bfTime = bf.time_ms;
        const dijSteps = dijk.steps.length;
        const bfIters = bf.steps.length;

        function winnerClass(a, b) {
            if (a < b) return 'class="winner"';
            if (a > b) return '';
            return '';
        }

        cmpTableWrap.innerHTML = `
            <table class="cmp-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Dijkstra</th>
                        <th>Bellman-Ford</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Relaxations</td>
                        <td ${winnerClass(dijRelax, bfRelax)}>${dijRelax}</td>
                        <td ${winnerClass(bfRelax, dijRelax)}>${bfRelax}</td>
                    </tr>
                    <tr>
                        <td>Steps / Iterations</td>
                        <td>${dijSteps}</td>
                        <td>${bfIters}</td>
                    </tr>
                    <tr>
                        <td>Execution Time (ms)</td>
                        <td ${winnerClass(dijTime, bfTime)}>${dijTime}</td>
                        <td ${winnerClass(bfTime, dijTime)}>${bfTime}</td>
                    </tr>
                    <tr>
                        <td>Handles Negative Weights</td>
                        <td><span class="tag tag-red">No</span></td>
                        <td><span class="tag tag-green">Yes</span></td>
                    </tr>
                    <tr>
                        <td>Detects Negative Cycles</td>
                        <td><span class="tag tag-red">No</span></td>
                        <td><span class="tag tag-green">Yes</span> ${bf.negative_cycle ? "(found!)" : ""}</td>
                    </tr>
                    <tr>
                        <td>Time Complexity</td>
                        <td>O((V+E) log V)</td>
                        <td>O(V * E)</td>
                    </tr>
                </tbody>
            </table>
        `;

        // Distance tables
        cmpDijDist.textContent = formatDistTable(dijk.distances, source);
        cmpBfDist.textContent = formatDistTable(bf.distances, source);

        // Graphs with shortest path trees
        const dijTreeEdges = new Set(dijk.tree_edges.map(e => `${e.from}->${e.to}`));
        const bfTreeEdges = new Set(bf.tree_edges.map(e => `${e.from}->${e.to}`));
        const dijVisited = new Set(dijk.steps.map(s => s.node));

        const dijNodeClasses = {};
        dijNodeClasses[source] = "source-node";
        const bfNodeClasses = {};
        bfNodeClasses[source] = "source-node";

        renderGraph(cmpDijSvg, data.graph, data.positions, {
            visitedNodes: dijVisited,
            treeEdges: dijTreeEdges,
            nodeClasses: dijNodeClasses,
            distMap: dijk.distances,
        });

        const bfVisited = new Set();
        for (const n of data.graph.nodes) {
            if (bf.distances[n] !== "inf") bfVisited.add(n);
        }

        // Negative cycle edges
        const negcycleEdges = new Set();
        const negcycleNodes = new Set();
        if (bf.negative_cycle) {
            bf.negative_cycle_edges.forEach(e => {
                negcycleEdges.add(`${e.from}->${e.to}`);
                negcycleNodes.add(e.from);
                negcycleNodes.add(e.to);
            });
        }

        renderGraph(cmpBfSvg, data.graph, data.positions, {
            visitedNodes: bfVisited,
            treeEdges: bfTreeEdges,
            negcycleEdges,
            negcycleNodes,
            nodeClasses: bfNodeClasses,
            distMap: bf.distances,
        });
    });


    // =================================================================
    // 4. CAMPUS MAP DEMO
    // =================================================================

    const campusSource = document.getElementById("campus-source");
    const campusTarget = document.getElementById("campus-target");
    const campusRun    = document.getElementById("campus-run");
    const campusInit   = document.getElementById("campus-init");
    const campusSvg    = document.getElementById("campus-svg");
    const campusResult = document.getElementById("campus-result");
    const campusDistTable = document.getElementById("campus-dist-table");

    let campusGraphData = null;
    let campusPositions = null;

    campusInit.addEventListener("click", async () => {
        const data = await apiPost("/api/campus/init", {});
        campusGraphData = data.graph;
        campusPositions = data.positions;

        // Populate dropdowns
        campusSource.innerHTML = "";
        campusTarget.innerHTML = "";
        data.buildings.forEach(b => {
            const opt1 = document.createElement("option");
            opt1.value = b;
            opt1.textContent = b.replace(/_/g, " ");
            campusSource.appendChild(opt1);
            const opt2 = document.createElement("option");
            opt2.value = b;
            opt2.textContent = b.replace(/_/g, " ");
            campusTarget.appendChild(opt2);
        });
        // Default selection
        if (data.buildings.length > 1) {
            campusTarget.value = data.buildings[data.buildings.length - 1];
        }

        renderGraph(campusSvg, campusGraphData, campusPositions);
        campusResult.textContent = "Select buildings and click 'Find Route'.";
        campusDistTable.textContent = "";
    });

    campusRun.addEventListener("click", async () => {
        if (!campusGraphData) {
            alert("Load the campus map first.");
            return;
        }
        const source = campusSource.value;
        const target = campusTarget.value;
        if (!source || !target) { alert("Select both buildings."); return; }
        if (source === target) { alert("Select different buildings."); return; }

        const data = await apiPost("/api/campus/path", { source, target });
        if (data.error) {
            alert(data.error);
            return;
        }

        const path = data.path;
        const dist = data.path_distance;
        const result = data.result;

        // Highlight path
        const pathNodes = new Set(path);
        const pathEdges = new Set();
        for (let i = 0; i < path.length - 1; i++) {
            pathEdges.add(`${path[i]}->${path[i+1]}`);
            pathEdges.add(`${path[i+1]}->${path[i]}`);
        }

        // Tree edges
        const treeEdges = new Set(result.tree_edges.map(e => `${e.from}->${e.to}`));

        const nodeClasses = {};
        nodeClasses[source] = "source-node";
        nodeClasses[target] = "target-node";

        renderGraph(campusSvg, data.graph, data.positions, {
            pathNodes,
            pathEdges,
            treeEdges,
            nodeClasses,
            distMap: result.distances,
        });

        if (path.length > 0) {
            // Build step-by-step route description
            let routeDesc = `Shortest route from ${source.replace(/_/g, " ")} to ${target.replace(/_/g, " ")}:\n\n`;
            routeDesc += `Total walking time: ${dist} minutes\n`;
            routeDesc += `Path: ${path.map(n => n.replace(/_/g, " ")).join(" -> ")}\n\n`;
            routeDesc += "Route breakdown:\n";
            for (let i = 0; i < path.length - 1; i++) {
                // Find edge weight
                const edge = data.graph.edges.find(e =>
                    (e.from === path[i] && e.to === path[i+1]) ||
                    (e.from === path[i+1] && e.to === path[i])
                );
                const w = edge ? edge.weight : "?";
                routeDesc += `  ${path[i].replace(/_/g, " ")} -> ${path[i+1].replace(/_/g, " ")}: ${w} min\n`;
            }
            campusResult.textContent = routeDesc;
        } else {
            campusResult.textContent = `No route found from ${source} to ${target}.`;
        }

        // All distances
        campusDistTable.textContent = formatDistTable(result.distances, source);
    });

    // Auto-load campus map
    campusInit.click();

});
