const {Client,Contact} = require('whatsapp-web.js');
const qrcode=require('qrcode-terminal');
const readline=require('readline');
const rl=require('readline-sync');
const client = new Client();
const contact=new Contact();
var num=rl.question("Enter Admin Number: ");
console.log("Entered Admin Number: "+num);
console.clear();
console.log("Generating QR for "+num+"...");

client.on('qr', (qr) => {
    qrcode.generate(qr, {small: true});
});

//console.log("Num Test: "+num);
client.on('ready', () => {
//  console.clear();
  console.log('Client is ready!');
 });
 
 client.on('message', async (message) => {
console.log(`New message received: ${message.body} from ${message.from}`);
var numlist=['9645703000','9072001357'];
var leng=numlist.length;
var i=0,c=0;
var exi;
var numm=[];
var msg='abc';
//:topp
//var op=rl.question("Send Message Menue:\n1.Text Message\n2.Image Message\n3.Exit\nChoose Option: ");
//switch(op)
{
	//case 1:
	for(i=0;i<leng;i++)
	{
		const user = await client.getNumberId(numlist[i]);	//await
		const chatId = user._serialized;
		msg=rl.question("Enter message to be sent: ");
		console.log('\nNumber(Reciever): '+numlist[i]+'\n'+'Message: '+msg);
		c=rl.question("Are the details correct[1/0]: ");
		if(c==1)
		{
			client.sendMessage(chatId,msg);
			console.log("Message Sent Succesfully!");
		}
		else
		{
			msg=rl.question("Enter message(Correction): ");
			console.log("\nMessage Updated Succesfully!");
		}
	}
	exi=rl.question("\nDo you want to continue(1/0): ");
	//if(exi==0)
		//break;
	/*break;
	case 2:
	for(i=0;i<leng;i++)
	{
		const user = await client.getNumberId(numlist[i]);	//await
		const chatId = user._serialized;
		var ip=rl.question("Enter Image Path: ");
		var capt=rl.question("Enter Caption for Image: ");
        sendImage(chatId, ip,capt);
	}
	exi=rl.question("\nDo you want to continue(1/0): ");
	if(exi==0)
		break;
	case 3: console.log("Press ctrl+c to exit...");
			break;
	break;
	default: console.log("Wrong Option!!");
	break;*/
}
 });
 
 async function sendImage(number, imagePath, caption) {
  try {
    // Get the chat by the number
    const chat = await client.getChatById(number);

    // Read the image file as a buffer
    const imageBuffer = fs.readFileSync(imagePath);

    // Send the image
    await chat.sendFile(imageBuffer, 'image.jpg', { caption });

    console.log('Image sent successfully');
  } catch (error) {
    console.error('Error sending image:', error);
  }
}
 client.initialize();