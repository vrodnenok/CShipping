$(function() {
    $.get("/xhr_test", function(data) {
       // alert(data);
    });
});

// $('#q').hide();

var Vessels = {

    init: function(config){
        this.config=config;
        this.bindEvents();
        $.ajaxSetup({
            url: 'index.php',
            type: 'POST'
        })
    },
    
    bindEvents: function(){
        this.config.vesselSelection.click(this.get_voyages_list);
        this.config.voyageSelection.click(this.get_operations);
        this.config.actorList.on('click', 'li', this.displayAuthorsInformation);
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
    
    displayAuthorsInformation: function(e){
        var self=Vessels;
        
        $.ajax({
            data: {actor_id: $(this).data('actor_id')},
            
        }).then(function(results){
            self.config.actorInfo.html(self.config.actorInfoTemplate({info:results}));
        });
        
        e.preventDefault();
    },
    
    get_voyages_list : function () {
    $("#vg").empty();
    $.post("/xhr_test", {
        vsl_id: $("#q").val()
     },
    function(data) {
        $("#vg").append(data);
    });
    },
    
    get_operations: function(){
        alert($('#vg').val());
    $.post("/xhr_test", {
        voy_id: $("#vg").val()
     },
    function(data) {
        alert(data);
        $("#operations").html(data);
    });
    }
}

Vessels.init({
    vesselSelection: $('#q'),
    voyageSelection: $('#vg'),
    form: $('#vessel_selection'),
    vesselListTemplate: $('#actors_list_template').html(),
    vesselInfoTemplate: $('#actors_info_template').html(),
    voyageList: $('ul.actors_list'),
    voyageInfo: $('div.actor_info')
});

