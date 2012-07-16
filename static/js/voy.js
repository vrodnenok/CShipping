// the voya management scripts

var Voyages = {

    init: function(config){
        alert('init');
        this.config=config;
        this.bindEvents();
        $.ajaxSetup({
            url: '/voyages/update/',
            type: 'POST',
            dataType: 'text',
            error: function(XMLHttpRequest, textStatus, errorThrown) 
            {console.log("An error has occurred: " + textStatus);
        }

      })
    },
    
    bindEvents: function(){
        this.config.addOnePort.click(this.addPort);
    },

    addPort: function(){
    //alert('add button has been pressed!');
    var $this= $(this);
    //alert ($this.parent().parent().text());
    var $trow = $this.parent().parent().find('td'); //.eq(0).children().children().val());
    alert($trow.eq(3).children().val());
        
        $.ajax({
            data:{
                action: 'add_port',
                voyages_id: $('#voyages_id').val(),
                port: $trow.eq(0).children().val(),
                turn: $trow.eq(1).children().val(),
                ops_type: $trow.eq(2).children().val(),
                agent: $trow.eq(3).children().val(),
                cargo: $trow.eq(4).children().val(),
                ldrate: $trow.eq(5).children().val(),
                est_da: $trow.eq(6).children().val(),
                
            },
        success: function(results){
            console.log(results);
        }
        }) 
    },

     
    manage_dist: function(){
        window.open ('/distances','_self',false)
    },
}

Voyages.init({
    addOnePort: $('#but_add'),
//    form: $('#vessel_selection'),
    });

