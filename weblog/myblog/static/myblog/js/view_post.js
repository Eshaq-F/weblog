var formatOptions = {weekday: 'long', day: 'numeric', month: 'long'}
var fullDateTime = now.toLocaleDateString("fa-IR", [formatOptions, "year", "month", "day"])
fullDateTime += " ; " + now.toLocaleTimeString("fa-IR")
$("#pub-date").html(fullDateTime)
$("#gist86057151").hide()
