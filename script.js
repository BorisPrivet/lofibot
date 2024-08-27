var play_button = document.getElementById('play_button')
var stop_button = document.getElementById('stop_button')
var audio = document.getElementById('radiowave')

if (audio.paused == true)
{
    play_button.onclick = function audioOn()
    {
        audio.play()
    }
}
else (audio.paused == false)
{
    stop_button.onclick = function audioOff()
    {
        audio.pause()
    }
}