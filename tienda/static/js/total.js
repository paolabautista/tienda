

function evaluar(){


	costo=document.getElementById('costo').value;
	existencias=document.getElementById('existencias').value;
	cantidad =document.getElementById('cantidad').value;
	total =document.getElementById('total');
	por = '*'

	if(cantidad >0 && existencias > cantidad-0 ){
		document.getElementById('pagar').disabled=false;	
	}
	else{
		document.getElementById('pagar').disabled=true;
	}

	total.value ='';
	total.value += costo += por += cantidad;

	igual = eval(document.getElementById('total').value);
	document.getElementById('total').value = igual;
	
	
	
	console.log(total);
	console.log(costo);
	console.log(existencias);
	console.log(cantidad);
}
