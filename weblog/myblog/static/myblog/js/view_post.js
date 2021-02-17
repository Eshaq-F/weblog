var formatOptions = {weekday: 'long', day: 'numeric', month: 'long'}
var fullDateTime = now.toLocaleDateString("fa-IR", [formatOptions, "year", "month", "day"])
fullDateTime += " ; " + now.toLocaleTimeString("fa-IR")
$("#pub-date").html(fullDateTime)
$("#gist86057151").hide()

$('.like').click(sample)
//$('.dislike').click(sample)
function sample() {
  var $btnId = $(this).attr('id')
  $('#' + $btnId + ' i').addClass("text-success")
  $('#' + $btnId.replace('-l', '-d') + ' i').removeClass("text-danger")
  console.log('ok')
//  $.post('/myblog/all_posts/', {'id': $btnId, 'like_dislike': true}, () => console.log('send...'))
}
