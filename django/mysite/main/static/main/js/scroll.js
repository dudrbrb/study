window.addEventListener('load', ()=>{
    var pageIdx = 0,
        initialX = null,
        initialY = null,
        nav = document.querySelector('aside'),
        sections = document.querySelectorAll('section');
    
    var initTouch = e => {
        initialX = `${e.touches ? e.touches[0].clientX : e.clientX}`;
        initialY = `${e.touches ? e.touches[0].clientY : e.clientY}`;
    };
    
    var swipeDirection = (e, act) => {
        if(act == 'wheel'){
            if(e.deltaY > 0){
                if(pageIdx !== 2){++pageIdx}
            }else{
                if(pageIdx !== 0){--pageIdx}
            }
            
        }
        else{
            if (initialX !== null && initialY !== null) {
                const currentX = `${e.touches ? e.touches[0].clientX : e.clientX}`,
                    currentY = `${e.touches ? e.touches[0].clientY : e.clientY}`;
            
                let diffX = initialX - currentX,
                    diffY = initialY - currentY;
            
            
                if(Math.abs(diffX) > Math.abs(diffY)){
                    if( 0 < diffX){
                        if(pageIdx !== 2){++pageIdx}
                    }else{
                        if(pageIdx !== 0){--pageIdx}
                    }
                }
            
                initialX = null;
                initialY = null;
            }
        }
        sections[pageIdx].scrollIntoView({behavior: "smooth", block: 'start'});
        pageIdx == 0 ? nav.classList.remove('b') : nav.classList.add('b') ;
    }
    
    window.addEventListener("touchstart", initTouch);
    window.addEventListener("touchmove", swipeDirection);
    window.addEventListener("mousedown", (e) => {
        initTouch(e),
        window.addEventListener("mousemove", swipeDirection)
    });
    window.addEventListener("mouseup", () => {
        window.removeEventListener("mousemove", swipeDirection);
    });
    addEventListener("mousewheel",  e => swipeDirection(e, 'wheel'))
})