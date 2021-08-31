/**
 * Created by Arty on 31.10.2018.
 */
$(function(){
    const smodal = $("#subscribe-modal");
    if(!smodal.length){
        return false;
    }

    const currDate = new Date();
    const previousShow = window.localStorage.getItem("KMASubscribe.lastShow")
        ? new Date(window.localStorage.getItem("KMASubscribe.lastShow"))
        : undefined;
    const counter = window.localStorage.getItem("KMASubscribe.counter")
        ? parseInt(window.localStorage.getItem("KMASubscribe.counter"))
        : 0;
    const period = window.localStorage.getItem("KMASubscribe.period")
        ? parseInt(window.localStorage.getItem("KMASubscribe.period"))
        : (1);
    const day = 3600*24*1000;

    if( (counter < 5)
        && (!previousShow || (currDate - previousShow >= period*day)) ){
        smodal.modal("show");
        window.localStorage.setItem("KMASubscribe.lastShow",currDate);
        window.localStorage.setItem("KMASubscribe.counter", counter+1);
        window.localStorage.setItem("KMASubscribe.period", period);
    }
/*
    if(!TextBack){
        console.log("TextBack didn't load");
        return false;
    }
    const widgetId = smodal.find("tb-notification-widget").attr("widget-id");
    const widgetInstance = TextBack.NotificationWidget.getWidget(widgetId);
    widgetInstance.then(
        result => {
           var channelList = result.config.channels;
           channelList[1].enabled = false;
           result.widget.channels[1].enabled = false;
            const subscribedChannelList = result.widgetSubscriptions;
            if( (counter < 5)
                && (!previousShow || (currDate - previousShow >= period*day))
                //&& (channelList.length > subscribedChannelList.length) ){ если есть неподписанные каналы
                && (!subscribedChannelList.length) ){ //если нет ни одного опдписанного канала
                smodal.modal("show");
                window.localStorage.setItem("TB.lastShow",currDate);
                window.localStorage.setItem("TB.counter", counter+1);
                window.localStorage.setItem("TB.period", period);
            }
        },
        result => {console.log("can't load TB widget instance")}
    );

*/


})