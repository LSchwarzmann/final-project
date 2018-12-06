/*
  This file stores the JavaScript syntax to generate the file tables on the website that display
  the sentiment analysis data. These functions are referenced by file_transaction.html and index.js
*/


// Creates a table to display the high level sentiment analysis
function create_sentiment_table(obj) {
    // Get table to modify
    let table = document.getElementById("sentiment");

    // Check if header has not been created, create it
    if (!document.getElementById("header_sent")) {
        // Create caption for table
        let caption = document.createElement("caption");
        $(caption).css({
            "text-align": "center",
            "caption-side": "top"
        });
        // Create attribute to indicate header has been created
        caption.setAttribute("id", "header_sent");
        caption.innerHTML = "General Sentiment Analysis"
        table.appendChild(caption);

        // Create actual header contents by appending it to the table
        let thead = document.createElement("thead");
        let th1 = document.createElement("th");
        let th2 = document.createElement("th");
        let node1 = document.createTextNode("Sentiment score");
        let node2 = document.createTextNode("Sentiment magnitude");
        th1.appendChild(node1);
        th2.appendChild(node2);
        thead.appendChild(th1);
        thead.appendChild(th2);
        table.appendChild(thead);
    }

    // Create table row of variables
    let row = table.insertRow(0);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    cell1.innerHTML = obj["sentiment"]["score"];
    cell2.innerHTML = obj["sentiment"]["magnitude"];
}

// Creates a table to display the classification
function create_classify_table(obj) {
    // Get table to modify
    let table = document.getElementById("classify");

    // Check if header has not been created, create it
    if (!document.getElementById("header_classify")) {
        // Create caption for table
        let caption = document.createElement("caption");
        $(caption).css({
            "text-align": "center",
            "caption-side": "top"
        });
        // Create attribute to indicate header has been created
        caption.setAttribute("id", "header_classify");
        caption.innerHTML = "Topic classification"
        table.appendChild(caption);

        // Create actual header contents by appending it to the table
        let thead = document.createElement("thead");
        let th1 = document.createElement("th");
        let th2 = document.createElement("th");
        let node1 = document.createTextNode("Name");
        let node2 = document.createTextNode("Confidence");
        th1.appendChild(node1);
        th2.appendChild(node2);
        thead.appendChild(th1);
        thead.appendChild(th2);
        table.appendChild(thead);
    }

    // Create table rows of variables
    for (let i = 0; i < obj["classify"].length; i++) {
        let row = table.insertRow(i);
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        cell1.innerHTML = obj["classify"][i]["name"];
        cell2.innerHTML = obj["classify"][i]["confidence"];
    }
}

// Creates a table to display the entities
function create_entity_table(obj) {
    // Get table to modify
    let table = document.getElementById("entities");

    // Check if header has not been created, create it
    if (!document.getElementById("header_entity")) {
        // Create caption for table
        let caption = document.createElement("caption");
        $(caption).css({
            "text-align": "center",
            "caption-side": "top"
        });
        // Create attribute to indicate header has been created
        caption.setAttribute("id", "header_entity");
        caption.innerHTML = "Entity analysis"
        table.appendChild(caption);

        // Create actual header contents by appending it to the table
        let thead = document.createElement("thead");
        let th1 = document.createElement("th");
        let th2 = document.createElement("th");
        let th3 = document.createElement("th");
        let node1 = document.createTextNode("Name");
        let node2 = document.createTextNode("Type");
        let node3 = document.createTextNode("Salience");
        th1.appendChild(node1);
        th2.appendChild(node2);
        th3.appendChild(node3);
        thead.appendChild(th1);
        thead.appendChild(th2);
        thead.appendChild(th3);
        table.appendChild(thead);
    }

    // Create table rows of variables
    for (let i = 0; i < obj["entities"].length; i++) {
        let row = table.insertRow(i);
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        let cell3 = row.insertCell(2);
        cell1.innerHTML = obj["entities"][i]["name"];
        cell2.innerHTML = obj["entities"][i]["type"];
        cell3.innerHTML = obj["entities"][i]["salience"];
    }
}


// Creates a table to display the syntax elements
function create_syntax_table(obj) {
    // Get table to modify
    let table = document.getElementById("syntax");

    // Check if header has not been created, create it
    if (!document.getElementById("header_syntax")) {
        // Create caption for table
        let caption = document.createElement("caption");
        $(caption).css({
            "text-align": "center",
            "caption-side": "top"
        });
        // Create attribute to indicate header has been created
        caption.setAttribute("id", "header_syntax");
        caption.innerHTML = "Syntax analysis"
        table.appendChild(caption);

        // Create actual header contents by appending it to the table
        let thead = document.createElement("thead");
        let th1 = document.createElement("th");
        let th2 = document.createElement("th");
        let node1 = document.createTextNode("Tag");
        let node2 = document.createTextNode("Content");
        th1.appendChild(node1);
        th2.appendChild(node2);
        thead.appendChild(th1);
        thead.appendChild(th2);
        table.appendChild(thead);
    }


    // Create table rows of variables
    for (let i = 0; i < obj["syntax"].length; i++) {
        let row = table.insertRow(i);
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        cell1.innerHTML = obj["syntax"][i]["tag"];
        cell2.innerHTML = obj["syntax"][i]["content"];
    }
}