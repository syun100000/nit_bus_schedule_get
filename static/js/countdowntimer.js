    //カウンドダウンタイマーの関数　1秒ごとにページを更新
    function countdownTimer(time, id) {
        function getMillisecondsFromMidnight() {
            //午前0時からの経過時間をミリ秒で取得する関数
            let now = new Date();
            let midnight = new Date(now.getFullYear(), now.getMonth(), now.getDate());
            let milliseconds = now.getTime() - midnight.getTime();
            return milliseconds;
            }
        let nowTime = getMillisecondsFromMidnight();
        function mesget(time){
            //特定の時間のミリ秒を取得する関数
            let timeString = time;
            let parts = timeString.split(':');
            let date = new Date();
            date.setHours(parts[0], parts[1], 0, 0);
            let milliseconds = date.getHours() * 60 * 60 * 1000 + date.getMinutes() * 60 * 1000;
            console.log("リターン値",milliseconds);
            return milliseconds;
        }
        var countTime = mesget(time);
        console.log("現在時刻",nowTime);
        console.log("カウント値（目標）",countTime);
        var dms = countTime - nowTime;
        var m = Math.floor(dms / 1000 / 60);
        console.log("分",m);
        var s = Math.floor((dms / 1000) % 60);
        console.log("秒",s);
        var timer = document.getElementById(id);
        console.log("発車まで: " + m + "分" + s + "秒")
        if (dms > 3600000) {
            timer.innerHTML = "発車まで: 1時間以上";
            setInterval(() => countdownTimer(time, id), 1000);
        } else if(dms > 0){
            timer.innerHTML = "発車まで: " + m + "分" + s + "秒";
            setInterval(() => countdownTimer(time, id), 1000);
        }
        else {
            timer.innerHTML = "";
            setInterval(() => countdownTimer(time, id), 1000);
        }
}