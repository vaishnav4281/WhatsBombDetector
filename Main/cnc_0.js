const {Client,Contact,PrivateContact} = require('whatsapp-web.js');
const qrcode=require('qrcode-terminal');
const readline=require('readline');
const rl=require('readline-sync');

const client = new Client();
const contact=new Contact();
const pvtcnt=new PrivateContact();
/*const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter User No.: \n", numin=>{console.log("Given Number: "+numin)

//pause for 5 sec

console.log("Starting...");
setTimeout(() => {
  console.log("Paused for 5 seconds.");
}, 5000);
console.log("Finished.");


rl.close();	
});*/
//const atkr='';
var num=rl.question("Enter User Number: ");
console.log("Entered User Number: "+num);
console.clear();
console.log("Generating QR for "+num+"...");
client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});
//console.log("Num Test: "+num);
client.on('ready', () => {
//  console.clear();
  console.log('Client is ready!');
  //client.block(atkr);
  /*client.sendMessage(num, "Attack Found!!")
  .then(() => console.log('Message sent successfully!'))
  .catch((error) => console.error('Error sending message: ', error));*/
});

//var c,i;
//let i=0,c=0;
let i=0,j;
var msg=[];
var c=0,fact=5;
var spm=['Qwerty23','Test','Hack','#$#%@'];
const len=spm.length;

client.on('message', async (message) => {
  console.log(`New message received: ${message.body} from ${message.from}`);
// while(c==0){
//const chat = message.chat;
const atkr=message.from.replace('@c.us','');
const atkrr=message.from;
const contact=await message.getContact();
const usrnum=num+'@c.us';
const user = await client.getNumberId(num);	//await
const chatId = user._serialized;
const chat= await message.getChat();
msg=message.body;
//const number=atkr;
	//while(msg==true){
for(i=0;i<=fact;i++)
{
	if(msg==spm[i])
		c++;
	if(c==fact)
	{
		console.log('\nAttackFound!!!');
		console.log('User Number: '+num);
		console.log('Attacker Number: '+atkr);
		client.sendMessage(chatId, "Hey, the number "+atkr+" tried to Attack you!");
		//if(atkr==='number@s.whatsapp.net')
		//{
		//const chat=await message.getChat();
			//chat.contact.block();
		await contact.block(atkrr);
		console.log("Contact "+atkr+" blocked Succesfully!!\n");
		client.sendMessage(chatId,"Attacker Blocked Succesfully!");
		c=0;
		break;
	
		//}
		//client.sendMessage(num,"Attacker Blocked Succesfully!");
		
		
	}
}
	//  if(message.body[i] === message.body[i++]){
	//	  c=1;
	//	  console.log('Attack Found!!!');
	//  break;
//	i++;
//	 }
	// }
//	i++;
 //}
});



client.initialize();

