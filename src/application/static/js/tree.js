let svg = d3.select("#tree")
	.attr("width", 1500).attr("height", 800)
	.append("g").attr("transform", "translate(0, 50)");

let data = [
	{"child": "Business Course", "parent": "", "root": "root"},
		{"child": "AD1101", "parent": "Business Course"},
			{"child": "AD2101", "parent": "AD1101"},
			{"child": "BC2402", "parent": "AD1101"},
		{"child": "AB1201", "parent": "Business Course"},
			{"child": "BC0401", "parent": "AB1201"},
		{"child": "AB1301", "parent": "Business Course"},
			{"child": "BC2406", "parent": "AB1301"},
				{"child": "BE2601", "parent": "BC2406"},
				{"child": "AB3601", "parent": "BC2406"},
				{"child": "ET0001", "parent": "BC2406"},
		{"child": "AB1401", "parent": "Business Course"},
			{"child": "GC0001", "parent": "AB1401"},
			{"child": "AB0602", "parent": "AB1401"},
		{"child": "AB1202", "parent": "Business Course"},
			{"child": "BS2407", "parent": "AB1202"},
];

let dataStruc = d3.stratify()
	.id(function(d) {return d.child;})
	.parentId(function(d) {return d.parent;})
	(data);

let treeStruc = d3.tree().size([1000, 500]);
let info = treeStruc(dataStruc);
//console.log(info.descendants());
//console.log(info.links());

let connections = svg.append('g').selectAll("path")
	.data(info.links());

connections.enter().append("path")
	.attr('d', function(d) {
		return 'M' + d.source.x + ',' + d.source.y + " C " +
		d.source.x + ',' + (d.source.y + d.target.y)/2 + ' ' +
		d.target.x + ',' + (d.source.y + d.target.y)/2 + ' ' +
		d.target.x + ',' + d.target.y;
	});

let circles = svg.append('g').selectAll("circle")
	.data(info.descendants());

circles.enter().append("circle")
	.attr("cx", function(d) {return d.x;})
	.attr("cy", function(d) {return d.y;})
	.attr('r', 10)
	.attr("id", function(d) {
		if (d.data.root) {
			return d.data.root;
		}
		return d.data.child;
	})
	.attr("class", function(d) {
		if (taken.includes(d.data.child)) {
			return "alreadyCleared";
		}
		return "notCleared";
	});

let names = svg.append('g').selectAll("text")
	.data(info.descendants());

names.enter().append("text")
	.text(function(d) {return d.data.child;})
	.attr('x', function(d) {return d.x + 13;})
	.attr('y', function(d) {return d.y + 4;})
	.attr("id", function(d) {return d.data.child;});

	let selected = [];
	let allCircles = document.getElementsByTagName("circle");
	let index;
	let selectionDisplay = document.getElementById("selectedCoursesFromTree");

	for (let q = 0; q < allCircles.length; q++) {
		if (allCircles[q].id == "root" || taken.includes(allCircles[q].id)) {
			continue;
		}
		allCircles[q].classList.add("hoverEffects");
		allCircles[q].addEventListener("click", function(event) {
			if (selected.includes(event.target.id)) {
				index = selected.indexOf(event.target.id);
				selected.splice(index, 1);
			} else {
				selected.push(event.target.id);
			}
			console.log(selected);
			selectionDisplay.innerHTML = selected;
		})
	}



