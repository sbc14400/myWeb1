// onload는 script를 head tag에 위치시기고자 할때 사용
    // 그러나 속도적인 측면에서는 rendering 지연을 야기시킬수 있다.

window.onload = function(){
    var hw = document.getElementById('hw');
    var f =  function(){
        alert('Hello World Function')
    }
    hw.addEventListener('click', function(){
        alert('Hello world');
    })
    hw.addEventListener('mouseover', f)
}
