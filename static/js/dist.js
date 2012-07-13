//alert('imported script in action');
$('#add').click(addDistance);
$('#filter').on('input', findPorts);
bindEvents();

function bindEvents(){
    $('.update').click(updateDistance);
    $('.delete').click(deleteRecord);
}

function deleteRecord(){
    var row=$(this).parent().parent();
    
    var cols = row.find('td');
    alert(cols.eq(0).children().val());
        $.post("/distances/update", {
            action: 'delete',
            id : row.attr('value')
         },
        function(data) {
            console.log('Deleted: '+data);
            findPorts();
        });    
}

function findPorts(){
    //$(this).validate();
//    alert($(this).val());

        $.post("/distances/update", {
            action: 'find',
            filter: $('#filter').val(),
         },
        function(data) {
            $('#results').empty();
            $('#results').append(data);
            bindEvents();
            console.log('received: '+data);
        });

}

function updateDistance(){
    var row=$(this).parent().parent();
    
    var cols = row.find('td');
//    alert(cols.eq(0).children().val());
        $.post("/distances/update", {
            action: 'update',
            id : row.attr('value'),
            fport: cols.eq(0).children().val(),
            tport: cols.eq(1).children().val(),
            distance: cols.eq(2).children().val() 
         },
        function(data) {
            console.log('received: '+data);
        });
}

function addDistance(){
    var row=$(this).parent().parent();
    
    var cols = row.find('td');
        $.post("/distances/update", {
            action: 'add',
//            id : row.attr('value'),
            fport: cols.eq(0).children().val(),
            tport: cols.eq(1).children().val(),
            distance: cols.eq(2).children().val() 
         },
        function(data) {
            if (data == 'exists'){
                 alert ('this ports combination already exists!');
                 return;
             }
            alert(data); 
            location.reload();
            $('.add').each().empty();
            console.log('received: '+data);
        });
}
