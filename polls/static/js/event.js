/** events.html页面单独的JS */

$(function() {

(function($){
	var listPrev = $('.listPrev'), listNext = $('.listNext'), listBox = $('.listBox'), listTime = $('#listTime'),
		list = listBox.find('ul'), listAchor = list.find('li'),listText = listAchor.find('p'),
		
		scrollContent = $('.event-ajax'),
		//scrollblock = $('#scrollblock-events'),
		maxIuid = listAchor.length - 1;
		maxGuid = listAchor.length - 8;
		
	var heightRun = listBox.find('li').outerWidth(true), guid = 0, Iuid = 0;
	list.width(listAchor.length*heightRun);
	//绑定上一步下一步的事件
	var mainRun = function(i,y){
		//重置滚动条
		//scroll && scroll.unbind();
		//scrollblock.css('top','0px');
		//scrollContent.css('top','0px');
		//焦点
		y < 0 && (y = Iuid = 0);
		y > maxIuid && (y = Iuid = maxIuid);
		listAchor.removeClass('cur').eq(y).addClass('cur');
		//滚动
		i < 0 && (i = guid = 0);
		i > maxGuid && (i = guid = maxGuid);
		list.stop(true).animate({
			/*left:-i*heightRun*/
		});
		//时间
		var value = listAchor.eq(y).find('p').text();
		listTime.html(value);
		var menuId = listAchor.eq(y).find('p').attr("id");
		//ajax
		
		
		for(var i=1990;i<(value+1);i++){
			
			if(document.getElementById("dk_"+i)!=undefined){
				
			 document.getElementById("dk_"+i).style.display='none';}
			}
			document.getElementById("dk_"+value).style.display='block';
		
	}
	mainRun(guid, Iuid);
	listPrev.bind('click', function(){
		mainRun(++guid, ++Iuid);
	});
	listNext.bind('click', function(){
		mainRun(--guid, --Iuid);
	});
	listAchor.bind('click', function(e){
		e.preventDefault();
		Iuid = listAchor.index(this);
		mainRun(guid, Iuid);
	});
	

})($);



})