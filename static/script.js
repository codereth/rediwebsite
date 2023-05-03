var pics;
function animate(whichone){
    whichone %= pics.length;
    document.images["stickman"].src = pics[whichone];
    window.setTimeout("animate(" + (whichone + 1)+");",1000);
}
    window.onload   =  function()   {
    pics = new Array( "3.jpg","2.jpg","4.jpg","10.jpg","18.jpg","19.jpg","21.jpg","20.jpg");
    animate(0);
}
    // const d = new Date();
    // d.setFullYear(2020, 11, 3);
    // let array = document.querySelectorAll(".gallery-de-dis small");

    // array.forEach(element => {
    //     element.innerHTML = d;
    // });