"use client";

import { useEffect, useState } from "react";
import * as d3 from "d3";
import Head from "next/head";

export default function RenderMap({ data }) {
    const [rootNode, setRootNode] = useState(d3.hierarchy(data, d => d.sub_topics));

    useEffect(() => {
        console.log(data);
        console.log("useEffect is running");

        // Clear any existing SVG content
        d3.select("#mindmap-svg").selectAll("*").remove();

        const margin = { top: 20, right: 120, bottom: 20, left: 120 };
        const height = window.innerHeight - margin.top - margin.bottom;
        const width = window.innerWidth - margin.left - margin.right; // Initial width for SVG

        // Create SVG container
        const svg = d3
            .select("#mindmap-svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const tree = d3.tree().size([height, width / 1.5]);

        function update(root) {
            console.log("update called");

            rootNode.descendants().forEach(d => {
                if (d.depth === 1) {
                    console.log(d._children);

                }
            });
            tree(root);

            // Calculate SVG width and height dynamically
            const svgWidth = Math.max(Math.max(...root.descendants().map(d => d.y)), width) + margin.left + 50; // Add extra margin
            const svgHeight = Math.max(height, d3.max(root.descendants(), d => d.x)) + margin.bottom;
            d3.select("#mindmap-svg").attr("width", svgWidth).attr("height", svgHeight);

            const colorScale = d3.scaleOrdinal(d3.schemeSet3);

            // Tooltip div
            const tooltip = d3.select("#mindmap")
                .append("div")
                .attr("class", "tooltip")
                .style("opacity", 0);

            // Draw links
            const link = svg
                .selectAll(".link")
                .data(root.descendants().slice(1), d => d.id) // Use `id` to identify nodes
                .join(
                    enter => enter.append("path")
                        .attr("class", "link")
                        .attr("d", d => `
                            M${d.y},${d.x}
                            C${(d.y + d.parent.y) / 2},${d.x}
                            ${(d.y + d.parent.y) / 2},${d.parent.x}
                            ${d.parent.y},${d.parent.x}
                        `)
                        .style("fill", "none")
                        .style("stroke", "#ccc")
                        .style("stroke-width", "2px"),
                    update => update
                        .attr("d", d => `
                            M${d.y},${d.x}
                            C${(d.y + d.parent.y) / 2},${d.x}
                            ${(d.y + d.parent.y) / 2},${d.parent.x}
                            ${d.parent.y},${d.parent.x}
                        `),
                    exit => exit.remove()
                );

            // Draw nodes
            const node = svg
                .selectAll(".node")
                .data(root.descendants(), d => d.id) // Use `id` to identify nodes
                .join(
                    enter => enter.append("g")
                        .attr("class", "node")
                        .attr("transform", d => `translate(${d.y},${d.x})`)
                        .on("click", (event, d) => {
                            if (d.data.link) {
                                window.open(d.data.link, "_blank");
                            }
                        })
                        .on("mouseover", (event, d) => {
                            tooltip.transition().duration(200).style("opacity", .9);
                            tooltip.html(d.data.text)
                                .style("left", `${event.pageX + 5}px`)
                                .style("top", `${event.pageY - 28}px`);
                        })
                        .on("mouseout", () => {
                            tooltip.transition().duration(500).style("opacity", 0);
                        }),
                    update => update
                        .attr("transform", d => `translate(${d.y},${d.x})`),
                    exit => exit.remove()
                );

            // Add circle background for nodes
            node.append("circle")
                .attr("r", 15)
                .style("fill", (d) => colorScale(d.depth))
                .style("stroke", "#000")
                .style("stroke-width", "0.5px");

            // Add URL icon for nodes with a link
            //const linkIconBase64 = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICA8cGF0aCBkPSJNMTIgNGwtMi0yTDYuOTUgMTMuOTZMMjAuMyA2Ljc1bDEuMjUgMS4yNWwxLjI1LTEuMjVMMi4yMCA4LjUsNCAxNiIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtY29sb3I9IiMzMzMiLz48L3N2Zz4=";

            // Handle icons
            //const icon = node
            //    .selectAll("image")
            //    .data(d => d.data.link ? [d] : [], d => d.id) // Only bind data if node has a link
            //    .join(
            //        enter => enter.append("svg:image")
            //            .attr("xlink:href", linkIconBase64)
            //            .attr("width", 20) // Adjust size if necessary
            //            .attr("height", 20) // Adjust size if necessary
            //            .attr("x", -15) // Adjust positioning if necessary
            //            .attr("y", -40) // Move the icon slightly above the node
            //            .style("cursor", "pointer")
            //            .on("click", (event, d) => {
            //                if (d.data.link) window.open(d.data.link, "_blank");
            //            }),
            //        update => update,
            //        exit => exit.remove()
            //    );

            // Add text
            const text = node
                .selectAll("text")
                .data(d => [d], d => d.id) // Bind text to nodes
                .join(
                    enter => enter.append("text")
                        .attr("dy", "0.35em")
                        .attr("x", d => (d.depth !== 2 ? -20 : 20))
                        .style("text-anchor", d => (d.depth !== 2 ? "end" : "start"))
                        .style("font", "16px sans-serif")
                        .style("font-weight", "bolder")
                        .text(d => d.depth === 2 ? `${d.data.name} : ${d.data.text || ''}` : d.data.name)
                        .each(function (d) {
                            const bbox = this.getBBox();
                            const nodeColor = colorScale(d.depth);
                            function getContrastYIQ(hexcolor) {
                                hexcolor = hexcolor.replace("#", "");
                                const r = parseInt(hexcolor.substr(0, 2), 16);
                                const g = parseInt(hexcolor.substr(2, 2), 16);
                                const b = parseInt(hexcolor.substr(4, 2), 16);
                                const yiq = (r * 299 + g * 587 + b * 114) / 1000;
                                return yiq >= 128 ? "#333333" : "white";
                            }

                            const textColor = getContrastYIQ(nodeColor);

                            d3.select(this)
                                .style("fill", textColor);

                            if (textColor !== "#333333") {
                                d3.select(this).style("text-shadow", "1px 1px 2px rgba(0, 0, 0, 0.5)");
                            }

                            if (d.depth < 2) {
                                d3.select(this.parentNode).insert("rect", ":first-child")
                                    .attr("x", bbox.x - 10)
                                    .attr("y", bbox.y - 10)
                                    .attr("width", bbox.width + 15)
                                    .attr("height", bbox.height + 20)
                                    .attr("rx", 10) // Rounded edges
                                    .attr("ry", 10) // Rounded edges
                                    .style("fill", nodeColor)
                                    .style("stroke", "#495057")
                                    .style("stroke-width", "1px")
                                    .style("box-shadow", "0 4px 8px rgba(0, 0, 0, 0.1)");
                            }
                        })                    ,
                    update => update
                        .attr("x", d => (d.depth !== 2 ? -20 : 20))
                        .style("text-anchor", d => (d.depth !== 2 ? "end" : "start"))
                        .text(d => d.depth === 2 ? `${d.data.name} : ${d.data.text || ''}` : d.data.name),
                    exit => exit.remove()
                );

            // Add toggle buttons
            node
                .selectAll(".toggle")
                .data(d => d.children || d._children ? [d] : [], d => d.id) // Bind toggle data
                .join(
                    enter => enter.append("text")
                        .attr("class", "toggle")
                        .attr("x", 20)
                        .attr("dy", ".35em")
                        .text(d => d.children ? "\u2212" : "\u002B") // Unicode for minus and plus
                        .style("cursor", "pointer")
                        .on("click", (event, d) => {
                            console.log("Clicked");
                            event.stopPropagation();
                            if (d.children) {
                                d._children = d.children;
                                d.children = null;
                            } else {
                                d.children = d._children;
                                d._children = null;
                            }
                            // Update with new rootNode after toggle
                            update(root);
                        }),
                    update => update
                        .attr("x", 20)
                        .attr("dy", ".35em")
                        .text(d => d.children ? "\u2212" : "\u002B"),
                    exit => exit.remove()
                );

            // Add title
            node
                .selectAll("title")
                .data(d => [d], d => d.id) // Bind title data
                .join(
                    enter => enter.append("title")
                        .text(d => d.data.text),
                    update => update.text(d => d.data.text),
                    exit => exit.remove()
                );

        }
        // Collapse nodes at depth 2 by default
        rootNode.descendants().forEach(d => {
            if (d.depth === 1 && d.children !== null) {
                console.log(d.children);
                d._children = d.children;
                d.children = null;
            }

        });

        // Initial update
        update(rootNode);

        // Zoom and pan functionality
        const zoom = d3.zoom()
            .scaleExtent([0.5, 2])
            .on("zoom", (event) => {
                svg.attr("transform", event.transform);
            });

        d3.select("#mindmap-svg").call(zoom);

        console.log("Mind map created");

    }, [data]);

    return (
        <main>
            <Head>
                <title>Mind Map</title>
                <style>
                    {`
                    .tooltip {
                        position: absolute;
                        text-align: center;
                        padding: 10px;
                        font: 12px sans-serif;
                        background: rgba(0, 0, 0, 0.8);
                        color: white;
                        border-radius: 4px;
                        pointer-events: none;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        max-width: 300px;
                        word-wrap: break-word;
                    }

                    .scroll-container {
                        width: 100%;
                        height: 100vh;
                        overflow: auto;
                        position: relative;
                    }

                    svg {
                        display: block;
                        height: 100%;
                        width: auto; /* Adjust width based on content */
                    }
                    `}
                </style>
            </Head>
            <div className="scroll-container">
                <svg id="mindmap-svg"></svg>
            </div>
        </main>
    );
}
