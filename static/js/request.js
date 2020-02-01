$(document).ready(function () {
	$('#order-btn').click(function(){
		var shirtsPrice = 10;
		var jeansPrice = 10;
		var sheetsPrice = 30;
		var hoodiesPrice = 20;
		var noshirts = $('#shirts').val();
		var nojeans = $('#jeans').val();
		var nosheets = $('#bedsheets').val();
		var nohoodies = $('#hoodies').val();
		const count = parseInt(noshirts) + parseInt(nojeans) + parseInt(nosheets) + parseInt(nohoodies);
		$('#count').text(count)
		const shirtsFinalPrice = noshirts*shirtsPrice;
		console.log("short: "+shirtsFinalPrice);
		const jeansFinalPrice = nojeans*jeansPrice;
		console.log("jeans: "+jeansFinalPrice);
		const hoodiesFinalPrice = nohoodies*hoodiesPrice;
		console.log("hoodie: "+hoodiesFinalPrice);
		const sheetsFinalPrice = nosheets*sheetsPrice;
		console.log("sheets: "+sheetsFinalPrice);
		totalFinalPrice = shirtsFinalPrice+jeansFinalPrice+hoodiesFinalPrice+sheetsFinalPrice;
		$('#shirtsFinal').text("₹ "+shirtsFinalPrice);
		$('#jeansFinal').text("₹ "+jeansFinalPrice)
		$('#sheetsFinal').text("₹ "+sheetsFinalPrice)
		$('#hoodiesFinal').text("₹ "+hoodiesFinalPrice)
		$('#totalFinal').text("₹ "+totalFinalPrice)
		var randomId = Math.random().toString(36).substring(2, 8);
		console.log(randomId)
		// $('#recieptID').attr("href",randomId);
		$('#recieptID').val(randomId);
	});
	$('#getReciept-btn').click(function(){
		console.log('getReciept-btn called');
		var recieptId = $('#reciept').val();
		console.log(recieptId)
		const obj = {
			rId : recieptId
		}
		$.post('/fetchRec',obj,function(data){
			console.log(data[0],data[1],data[2],data[3])
			var shirtsPrice = 10;
			var jeansPrice = 10;
			var sheetsPrice = 30;
			var hoodiesPrice = 20;
			var noshirts = data[0];
			var nojeans = data[1];
			var nohoodies = data[2];
			var nosheets = data[3];
			
			const count = parseInt(noshirts) + parseInt(nojeans) + parseInt(nosheets) + parseInt(nohoodies);
		$('#count').text(count)
		const shirtsFinalPrice = noshirts*shirtsPrice;
		console.log("short: "+shirtsFinalPrice);
		const jeansFinalPrice = nojeans*jeansPrice;
		console.log("jeans: "+jeansFinalPrice);
		const hoodiesFinalPrice = nohoodies*hoodiesPrice;
		console.log("hoodie: "+hoodiesFinalPrice);
		const sheetsFinalPrice = nosheets*sheetsPrice;
		console.log("sheets: "+sheetsFinalPrice);
		totalFinalPrice = shirtsFinalPrice+jeansFinalPrice+hoodiesFinalPrice+sheetsFinalPrice;
		$('#shirtsCount').text(' x'+noshirts);
		$('#jeansCount').text(' x'+nojeans);
		$('#sheetsCount').text(' x'+nosheets);
		$('#hoodiesCount').text(' x'+nohoodies);
		$('#shirtsFinal').text("₹ "+shirtsFinalPrice);
		$('#jeansFinal').text("₹ "+jeansFinalPrice)
		$('#sheetsFinal').text("₹ "+sheetsFinalPrice)
		$('#hoodiesFinal').text("₹ "+hoodiesFinalPrice)
		$('#totalFinal').text("₹ "+totalFinalPrice)
		});
	});
}); 