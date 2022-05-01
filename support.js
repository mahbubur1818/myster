var startButton = document.querySelector("#middle_path");
var startButton2 = document.querySelector("#middle_path2");
	var tween = KUTE.fromTo(
	'#middle_path',
	 {path: '#middle_path' }, 
	 { path: '#middle_path2' },
	{repeat:999,duration:2000,yoyo:true}
	 ).start();

let cross = document.getElementById('cross');
let menu = document.getElementById('menu1');
let header2 = document.getElementById('header2');

cross.addEventListener('click',()=>{
header2.style.marginLeft = "-80%";
})

menu.addEventListener('click',()=>{
	header2.style.marginLeft = "0";
})