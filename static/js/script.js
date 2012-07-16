$(function() {
    $.get("/xhr_test", function(data) {
       // alert(data);
    });
});

var Vessels = {

    init: function(config){
        this.config=config;
        this.bindEvents();
        $.ajaxSetup({
            url: '/',
            type: 'POST'
        })
    },
    
    bindEvents: function(){
        this.config.vesselSelection.click(this.get_voyages_list);
        this.config.voyageSelection.click(this.get_operations);
        this.config.distanceManagement.click(this.manage_dist);
        this.config.voyageManagement.click(this.manage_voyage);
    },

    manage_voyage: function(){
        alert($("#q").val());
        window.open ('/voyages/vsl_id/'+$("#q").val()+'/voy_id/'+$("#vg").val(),'_self',false); 
    },   
       
    manage_dist: function(){
        window.open ('/distances','_self',false)
    },
      
      
    fetchVoyages: function(){
        var self = Vessels;
        $.ajax({
            data: self.config.form.serialize(),
            dataType: 'json',
            success: function(results){
                self.config.actorList.empty();
                if(results){
                    self.config.actorList.append(self.config.actorListTemplate(results));
                } else self.config.actorList.appent('No results were found!');
            }
        })
    },
    
   
    get_voyages_list : function () {
    $("#vg").empty();
    $('#operations').empty();
    $.post("/xhr_test", {
        vsl_id: $("#q").val()
     },
    function(data) {
        $("#vg").append(data);
    });
    },
    
    get_operations: function(){
        console.log($('#vg').val());
    $.post("/xhr_test", {
        voy_id: $("#vg").val()
     },
    function(data) {
        console.log(data);
        $("#operations").html(data);
        $('#operations').find('select').css('width', '100%')
        $('#operations').find('select').css('height', '100%')
        $('.tab_btn').on('click', operationFullEdit)
    });
    }
    
    
}

Vessels.init({
    vesselSelection: $('#q'),
    voyageSelection: $('#vg'),
    distanceManagement: $('#dist'),
    voyageManagement: $('#voyages'),
    form: $('#vessel_selection'),
    });

function operationFullEdit (){
    var $this= $(this);
    //alert ($this.parent().parent().text());
    alert($this.parent().siblings().eq(0).children().val());
}
