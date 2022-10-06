async function buildPlot() {
    const data = await d3.json("my_weather_data.json");
    const dateParser = d3.timeParse("%Y-%m-%d");
    const yAccessor = (d) => d.temperatureMin;
    const y1Accessor = (d) => d.temperatureHigh;
    const xAccessor = (d) => dateParser(d.date);
    // Функции для инкапсуляции доступа к колонкам набора данных

    var dimensions = {
        width: window.innerWidth * 0.9,
        height: 400,
        margin: {
            top: 15,
            right: 15,
            bottom: 15,
            left: 15,
        },
    };
    dimensions.boundedWidth =
        dimensions.width - dimensions.margin.left - dimensions.margin.right;
    dimensions.boundedHeight =
        dimensions.height - dimensions.margin.top - dimensions.margin.bottom;


    const wrapper = d3.select("#wrapper")
        .append("svg")
        .attr("width", dimensions.width)
        .attr("height", dimensions.height);



    const bounds = wrapper.append("g")
    bounds.style(
        "transform",
        `translate(${dimensions.margin.left}px,${dimensions.margin.top}px)`
    );


    const yScale = d3.scaleLinear()
        .domain([0,100])
        .range([dimensions.boundedHeight, 0]);
    const referenceBandPlacement = yScale(100);
    const referenceBand = bounds
        .append("rect")
        .attr("x", 0)
        .attr("width", dimensions.boundedWidth)
        .attr("y", referenceBandPlacement)
        .attr("height", dimensions.boundedHeight - referenceBandPlacement)
        .attr("fill", "#ffffff");

    const xScale = d3.scaleTime()
        .domain(d3.extent(data, xAccessor))
        .range([0, dimensions.boundedWidth]);


    const lineGenerator = d3.line()
        .x((d) => xScale(xAccessor(d)))
        .y((d) => yScale(yAccessor(d)))


    const lineGenerator2 = d3.line()
        .x((d) => xScale(xAccessor(d)))
        .y((d) => yScale(y1Accessor(d)))
        .curve(d3.curveBasis);


    const line = bounds
        .append("path")
        .attr("d", lineGenerator(data))
        .attr("fill", "none")
        .attr("stroke", "lightblue")
        .attr("stroke-width", 2);

    const line1 = bounds
        .append("path")
        .attr("d", lineGenerator2(data))
        .attr("fill", "none")
        .attr("stroke", "grey")
        .attr("stroke-width", 2);

    const yAxisGenerator = d3.axisLeft().scale(yScale);
    const yAxis = bounds.append("g").call(yAxisGenerator)


    const xAxisGenerator = d3.axisBottom().scale(xScale);
    const xAxis = bounds
        .append("g")
        .call(xAxisGenerator.tickFormat(d3.timeFormat("%d"+"."+"%m")))
        .style("transform", `translateY(${dimensions.boundedHeight}px)`);

    wrapper
        .append("g")
        .style("transform", `translate(${50}px,${15}px)`)
        .append("text")
        .attr("class", "title")
        .attr("x", dimensions.width / 2)
        .attr("y", dimensions.margin.top / 2)
        .style("font-size", "14px")
}

buildPlot();