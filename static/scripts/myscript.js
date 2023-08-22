// alert('Welcome to my web');


// 滑鼠 hover 事件，要放在 onload 外
function func(obj){
    console.log(obj.innerText);

}

window.onload=function(){


    // English checkbox
    var en = document.getElementById('english');

    en.addEventListener('change', e => {
        
        var td = document.querySelectorAll(".en");  
        var status = '';
        
        if(e.target.checked){
            // status = 'visible';
            status = 1;
        }
        else{ 
            // status = 'hidden';
            status = 0;        }
        
        for (i = 0; i < td.length; i++) {
            // td[i].style.visibility = status;
            td[i].style.opacity = status;
            
        }   
    
    });

    // Chinese checkbox
    var ch = document.getElementById('chinese');

    ch.addEventListener('change', e => {
        
        var td = document.querySelectorAll(".ch");  
        var status = '';
        
        if(e.target.checked){
            status = 1;
        }
        else{ 
            status = 0;
        }
        
        for (i = 0; i < td.length; i++) {
            td[i].style.opacity = status;
        }   
    
    });

    // collocation checkbox
    var ch = document.getElementById('collocation');

    ch.addEventListener('change', e => {
        
        var td = document.querySelectorAll(".co");  
        var status = '';
        
        if(e.target.checked){
            status = 1;
        }
        else{ 
            status = 0;
        }
        
        for (i = 0; i < td.length; i++) {
            td[i].style.opacity = status;
        }   
    
    });




  }







