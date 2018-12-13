# EstOk
EstOk is an errbot plugin, created to ease people's control of their house stock.
# Configuration
The EstOk is a plugin that has to be installed as a ordinary plugin in the errbot. You have to have a MongoDB installed in the machine as well, the code will automatically create the **collection** in the database, making unecessary to even handle with the mongo directly.
# Usage
The code atomatically create the objects in the database. The commands are: 

`adicionar` which will make the bot to ask the user which item he wants to add to the stock, the user should then anwser with the item. **Example:** `banana`;

`comprei`, which adds a quantity to the items that the user has already added, the user should anwser the bot after the command with the name of the item and the quantity **Example:** `banana 10`. After that the bot will tell the user how many he has now in the stock.;

`usei` , that removes a quantity from the items that the user has already, the user should anwser the bot after he asks with the name of the item and the quantity to be removed **Example:** `banana 5`, after that the bot will tell the user how many he has now in the stock.;

`estoque`, which informs the user how many of a item he has in the stock, the user should awnser the bot after the command with the name of the item. **Example:** `banana`, after that the bot will inform the user how many of the item he has in the stock.

**Note:** The objects are created using the Telegram ID of the users as the indentifier between the user, making possible for then only to access their own stock, and been not necessary to the user to indentify themselves.
