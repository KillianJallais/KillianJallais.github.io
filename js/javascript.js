function time() {
	var vtime = document.getElementById("time");
	var now = new Date();
	var jour = now.getDay();
	var heures = now.getHours();
	var minutes = now.getMinutes();

	if (heures<10){
		heures = "0"+heures;
	}

	if (minutes<10){
		minutes = "0"+minutes;
	}

	if (jour==0){
		jour = "Dimanche";
	}
	else if (jour==1){
		jour = "Lundi";
	}
	else if (jour==2){
		jour = "Mardi";
	}
	else if (jour==3){
		jour = "Mercredi";
	}
	else if (jour==4){
		jour = "Jeudi";
	}
	else if (jour==5){
		jour = "Vendredi";
	}
	else if (jour==6){
		jour = "Samedi";
	}

	vtime.innerHTML = jour + " " + heures + "h" + minutes;
}

function ease(x){
	return 6*Math.pow(x, 5)-15*Math.pow(x, 4)+10*Math.pow(x, 3);
}

function interpole(start, end, t){
	return start + t*(end - start);
}

function calcule_interpolation() {
	var A = Number(document.getElementById("A").value);
	var B = Number(document.getElementById("B").value);
	var C = Number(document.getElementById("C").value);
	var D = Number(document.getElementById("D").value);

	var X = Number(document.getElementById("X").value);
	var Y = Number(document.getElementById("Y").value);

	var FractX = ease(X - Math.floor(X));
	var FractY = ease(Y - Math.floor(Y));

	var AB = interpole(A, B, FractX);
	var CD = interpole(C, D, FractX);

	var value = interpole(AB, CD, FractY);

	alert("Le resultat est "+value);
}

function map(n, start1, stop1, start2, stop2) {
  return ((n-start1)/(stop1-start1))*(stop2-start2)+start2;
}

function bezier(points_X, points_Y, t){
	var j;
	if (points_X.length == 1){
		return [points_X[0], points_Y[0]];
	}
	else {
		let new_X = [];
		let new_Y = [];
		for (j = 0; j<points_X.length-1; j++){
			new_X.push(Math.trunc(baricentre(points_X[j], points_X[j+1], t)));
			new_Y.push(Math.trunc(baricentre(points_Y[j], points_Y[j+1], t)));
		}

		return bezier(new_X, new_Y, t);
	}
}

function baricentre(a, b, t){
	return (a*t)+(b*(1-t));
}

function draw() {
	var width;
	const canvas = document.getElementById('canvas');
	const ctx = canvas.getContext('2d');
	var size = document.getElementById("size").value;

	if (size == ""){
		size = "1";
	}

	ctx.clearRect(0, 0, 300, 300);

	let points_X = [170, 100, 70, 150];
	let points_Y = [120, 180, 90, 70];

	calcule(points_X, points_Y, size);

	points_X = [140, 260, 150, 140];
	points_Y = [72, 70, 20, 160];

	calcule(points_X, points_Y, size);

	points_X = [142, 142, 0, 190];
	points_Y = [150, 300, 180, 150];

	calcule(points_X, points_Y, size);

	points_X = [135, 15];
	points_Y = [285, 165];

	calcule(points_X, points_Y, width="1");

	points_X = [285, 165];
	points_Y = [165, 284];

	calcule(points_X, points_Y, width="1");

	points_X = [15, 135];
	points_Y = [135, 15];

	calcule(points_X, points_Y, width="1");

	points_X = [165, 285];
	points_Y = [15, 135];

	calcule(points_X, points_Y, width="1");

	points_X = [130, 150, 170];
	points_Y = [20, 0, 20];

	calcule(points_X, points_Y, width="1");

	points_X = [20, 0, 20];
	points_Y = [130, 150, 170];

	calcule(points_X, points_Y, width="1");

	points_X = [130, 150, 170];
	points_Y = [280, 300, 280];

	calcule(points_X, points_Y, width="1");

	points_X = [280, 300, 280];
	points_Y = [130, 150, 170];

	calcule(points_X, points_Y, width="1");
}

function calcule(points_X, points_Y, width) {
	var t = 0;
	var p = 40;
	var i;

	let valeur;

	let value_X = [];
	let value_Y = [];

	for (i = 0; i<p; i++){
		valeur = bezier(points_X, points_Y, t);

		value_X.push(valeur[0]);
		value_Y.push(valeur[1]);

		t += 1/p;
	}

	draw_courbe(value_X, value_Y, points_X, points_Y, width);
}

function draw_courbe(value_X, value_Y, points_X, points_Y, width) {
	var i;
	var a;
	var color = document.getElementById("color").value;
	const canvas = document.getElementById('canvas');
	const ctx = canvas.getContext('2d');
	ctx.lineWidth=width;
	const check = document.getElementById("check").checked;

	if (color == ""){
		color = "0";
	}
	else {
		color = parseFloat(color);
		color = map(color, 0, 1, 0, 255);
		color = Math.floor(color);
		color = String(color);
	}

	ctx.beginPath();
    ctx.moveTo(value_X[0], value_Y[0]);

    for (a = 1; a<value_X.length; a++){
    	ctx.lineTo(value_X[a], value_Y[a]);
    	ctx.strokeStyle = "rgb("+color+","+color+","+color+")";
    	ctx.stroke();
    }

    if (check){
    	for (i = 1; i<points_X.length-1; i++){
    		ctx.fillStyle = 'red';
			ctx.beginPath();
			ctx.arc(points_X[i], points_Y[i], 5, 0, 2 * Math.PI);
			ctx.fill();
    	}

	    ctx.fillStyle = 'blue';
		ctx.beginPath();
		ctx.arc(value_X[0], value_Y[0], 5, 0, 2 * Math.PI);
		ctx.arc(value_X[value_X.length-1], value_Y[value_Y.length-1], 5, 0, 2 * Math.PI);
		ctx.fill();
	}
}

function verif() {
	const name = document.getElementById("name").value;
	const first_name = document.getElementById("fist_name").value;
	const email = document.getElementById("email").value;
	const tel = document.getElementById("tel").value;

	if (name == "" || first_name == "" || email == "" || tel == ""){
		alert("Vous n'avez pas renseigné tous les champs du formulaire.");
		return false;
	}
	return true;
}