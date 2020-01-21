let a = document.getElementById('clickbtn');
let b = document.getElementById('changetext');
let o = b.innerHTML;
let u = 'changed';

a.onclick=function(){
  if(b.innerHTML==o){
    b.innerHTML=u;
  }
  else{
    b.innerHTML=o;
  }
};


$('#clickbtn2').click(function(){
  $('#changetext').toggle()
});

