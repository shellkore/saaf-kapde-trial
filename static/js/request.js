$(document).ready(function () {
	$('#order-btn').click(function(){
		var shirtsPrice = 5;
		var jeansPrice = 3;
		var sheetsPrice = 8;
		var hoodiesPrice = 2;
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
}); 