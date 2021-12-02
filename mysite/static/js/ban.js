var $typer = $('.typer'),
txt = $typer.data("text"),
tot = txt.length,
ch  = 0;

(function typeIt() {   
   if(ch > tot) return;
   $typer.text( txt.substring(0, ch++) );
   setTimeout(typeIt, ~~(Math.random()*(300-60+1)+60));
}());