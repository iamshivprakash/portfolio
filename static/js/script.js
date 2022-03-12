let scroll_up = document.querySelector('#scroll-up');

window.addEventListener('scroll',() =>{
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop >100){
        scroll_up.style.display = 'block';
    }else{
        scroll_up.style.display = 'none';
    }
})

scroll_up.addEventListener('click',() => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
})