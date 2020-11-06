window.onload=initAll;
function initAll() {
	var f=document.getElementById('f1');
	f.onclick=ff1;
	var f2=document.getElementById('f2');
	f2.onclick=ff2;
}
var otp='gg'
function ff1() {
	var hh1=document.getElementById('hh1');
	var email=document.getElementById('email').value;
	hh1.innerHTML='Please wait';
	url='/post_sign?email='+email;
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	     otp = xhttp.responseText;
	     document.getElementById('dv1').style.display="none";
	     document.getElementById('dv').style.display="block";
	     var f=document.getElementById('f1');
	     f.disabled =true;
	     var f2=document.getElementById('f2');
	    }
	  };
	xhttp.open("GET", url, true);
	xhttp.send();
}
function ff2() {
	console.log(otp);
	var o=document.getElementById('otp').value;
	var oo=o.toString();
	var x=otp.toString();
	if (oo==x) {
		var hh1=document.getElementById('hh1').innerHTML='success';
		var a=document.getElementById('aa');
		var username=document.getElementById('username').value;
		var pass_1=document.getElementById('pass_1').value;
		var pass_2=document.getElementById('pass_2').value;
		var email=document.getElementById('email').value;
		var last_name=document.getElementById('last_name').value;
		var first_name=document.getElementById('first_name').value;
		a.href='sign_2?username='+username+'&pass_1='+pass_1+'&pass_2='+pass_2+'&email='+email+'&first_name='+first_name+'&last_name='+last_name;
		a.click();
	}
	else{
		var hh1=document.getElementById('hh1').innerHTML='fails';
	}
}