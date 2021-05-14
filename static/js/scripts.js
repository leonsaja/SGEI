document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {
        hover: false,
        coverTrigger: false,
        alignment: 'left',
    });
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('select').formSelect();

});