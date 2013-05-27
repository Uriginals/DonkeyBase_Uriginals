function SelectMoveRows(leftBox,rightBox)
{
    var SelID='';
    var SelText='';
    // Move rows from left to right from bottom to top
    for (i=leftBox.options.length - 1; i>=0; i--)
    {
        if (leftBox.options[i].selected == true)
        {
            SelID=leftBox.options[i].value;
            SelText=leftBox.options[i].text;
            var newRow = new Option(SelText,SelID);
            rightBox.options[rightBox.length]=newRow;
            leftBox.options[i]=null;
        }
    }
    SelectSort(rightBox);
}
function SelectSort(SelList)
{
    var ID='';
    var Text='';
    for (x=0; x < SelList.length - 1; x++)
    {
        for (y=x + 1; y < SelList.length; y++)
        {
            if (SelList[x].text > SelList[y].text)
            {
                // Swap rows
                ID=SelList[x].value;
                Text=SelList[x].text;
                SelList[x].value=SelList[y].value;
                SelList[x].text=SelList[y].text;
                SelList[y].value=ID;
                SelList[y].text=Text;
            }
        }
    }
}

function selectAllOptions(inGroup, notInGroup)
{
  var inGroupObj = document.getElementById(inGroup);
  for (var i=0; i<inGroupObj.options.length; i++) {
    inGroupObj.options[i].selected = true;
  }
  var notInGroupObj = document.getElementById(notInGroup);
  for (var i=0; i<notInGroupObj.options.length; i++) {
    notInGroupObj.options[i].selected = true;
  }
  return true;
}