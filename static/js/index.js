$(document).ready(function() {
    var bsswitch = $(".BSSwitch");

    // Enable Switches
    bsswitch.bootstrapSwitch();

    //Add OnClickAJAX to Switches
    bsswitch.on('switchChange.bootstrapSwitch',function(event,state) {
        $.ajax({
            type : 'POST',
            url : '/togglelight',
            contentType : 'application/json',
            dataType : 'json',
            data : JSON.stringify({
                "id" : $(this).attr('id'),
                "on" : state
            })
        });
    });

    // Enable OnClickSelector for Scenes
    $(".sselector").click(function(e) {
        $(".sselector").removeClass("active");
        $(this).addClass("active");
        var hits = $(this).attr('data-hits');
        hits = parseInt(hits)+1;
        var name = $(this).attr('data-name');
        $(this).attr("data-hits", hits);
        $.ajax({
            type : 'POST',
            url : 'applyscene',
            contentType : 'application/json',
            dataType : 'json',
            data : JSON.stringify({
                "name" : name,
                "hue" : $(this).attr('data-hue'),
                "brightness" : $(this).attr('data-brightness'),
                "saturation" : $(this).attr('data-saturation'),
                "hits" : hits
            })
        });

        var span = $("span[id='"+name+"']");
        if (span[0] != null) {
            span[0].innerHTML= hits;
        }
        else {
            span.innerHTML= hits;
        }

        e.preventDefault();
    });

    // Enable OnClickSelector for Sounds
    $(".aselector").click(function(e) {
        var audio = document.getElementsByTagName("audio");
        //only one
        audio[0].setAttribute('src',$(this).attr('data-source'));
        audio[0].load();
        audio[0].play();
        $(".aselector").removeClass("active");
        $(this).addClass("active");
        e.preventDefault();
    });


});
