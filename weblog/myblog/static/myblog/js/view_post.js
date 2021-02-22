var formatOptions = {weekday: 'long', day: 'numeric', month: 'long'}
var fullDateTime = now.toLocaleDateString("fa-IR", [formatOptions, "year", "month", "day"])
fullDateTime += " ; " + now.toLocaleTimeString("fa-IR")
$("#pub-date").html(fullDateTime)
$("#gist86057151").hide()

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$('.like').click(like)
$('.dislike').click(dislike)

function like() {
  var $btnId = $(this).attr('id')
  var $likeNum = parseInt($('#' + $btnId).next().text())
  var $dislikeNum = parseInt($('#' + $btnId.replace('-l', '-d')).next().text())
  if ($('#' + $btnId.replace('-l', '-d') + ' i').hasClass('text-danger')){
    $('#' + $btnId.replace('-l', '-d') + ' i').removeClass("text-danger")
    $('#' + $btnId + ' i').addClass('text-success')
    $('#' + $btnId.replace('-l', '-d')).next().text($dislikeNum - 1)
    $('#' + $btnId).next().text($likeNum + 1)
    $.ajax({
        headers: {
            'X-CSRFTOKEN': csrftoken
        },
        type: "PUT",
        dataType: "json",
        url: "/myblog/comment_like_dislike/" + $btnId.replace('-l', '') + "/",
        data: {'like_dislike': true},
        success: function(data){
            console.log("PUT")
        }
    })
  }else if ($('#' + $btnId + ' i').hasClass('text-success')){
    $('#' + $btnId + ' i').removeClass('text-success')
    $('#' + $btnId).next().text($likeNum - 1)
    $.ajax({
        headers: {
            'X-CSRFTOKEN': csrftoken
        },
        type: "DELETE",
        url: "/myblog/comment_like_dislike/" + $btnId.replace('-l', '') + "/",
        success: function(status){
            console.log("DELETE")
        }
    })
  }else {
    $('#' + $btnId + ' i').addClass('text-success')
    $('#' + $btnId).next().text($likeNum + 1)
    $.post({url: "/myblog/comment_like_dislike/" + $btnId.replace('-l', '') + "/", headers: {'X-CSRFTOKEN': csrftoken},
    data: {'like_dislike': true}}).done(console.log('POST'))
  }
}

function dislike() {
  var $btnId = $(this).attr('id')
  var $dislikeNum = parseInt($('#' + $btnId).next().text())
  var $likeNum = parseInt($('#' + $btnId.replace('-d', '-l')).next().text())
  if ($('#' + $btnId.replace('-d', '-l') + ' i').hasClass('text-success')){
    $('#' + $btnId.replace('-d', '-l') + ' i').removeClass("text-success")
    $('#' + $btnId + ' i').addClass('text-danger')
    $('#' + $btnId.replace('-d', '-l')).next().text($likeNum - 1)
    $('#' + $btnId).next().text($dislikeNum + 1)
    $.ajax({
        headers: {
            'X-CSRFTOKEN': csrftoken
        },
        type: "PUT",
        dataType: "json",
        url: "/myblog/comment_like_dislike/" + $btnId.replace('-d', '') + "/",
        data: {'like_dislike': false},
        success: function(data){
            console.log("PUT")
        }
    })
  }else if ($('#' + $btnId + ' i').hasClass('text-danger')){
    $('#' + $btnId + ' i').removeClass('text-danger')
    $('#' + $btnId).next().text($dislikeNum - 1)
    $.ajax({
        headers: {
            'X-CSRFTOKEN': csrftoken
        },
        type: "DELETE",
        url: "/myblog/comment_like_dislike/" + $btnId.replace('-d', '') + "/",
        success: function(status){
            console.log("DELETE")
        }
    })
  }else {
    $('#' + $btnId + ' i').addClass('text-danger')
    $('#' + $btnId).next().text($dislikeNum + 1)
    $.post({url: "/myblog/comment_like_dislike/" + $btnId.replace('-d', '') + "/", headers: {'X-CSRFTOKEN': csrftoken},
    data: {'like_dislike': false}}).done(console.log("POST"))
  }
}
