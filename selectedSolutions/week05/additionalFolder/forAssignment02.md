# Basic Syntax for Markdown

## Overviews

Nearly all Markdown applications support the basic syntax outlined in the original Markdown design document. There are minor variations and discrepancies between Markdown processors - those are noted inline wherever possible.

## Headings

To create a heading, add number signs (#) in front of a word or phrase. The number of number signs you use should correspond to the heading level.
For example, to create a heading level three (<h3>), use three number signs.

```
### MIMPython
```

Markdown applications don't agree on how to handle a missing space between the number signs (#) and the heading name. For compatibility, always put a space between the number signs and the heading name.

You should also put blank lines before and after a heading for compatibility.

### Alternate Syntax

Alternatively, on the line below the text, add number of == characters for heading level 1 or - characters for heading level 2.

For example

```
Heading level 1
===============
```

## Paragraphs

To create paragraphs, use a blank line to separate one or more lines of text. Unless the paragraph is in a list, don't indent paragraphs with spaces or tabs.

### Line Breaks

To create a line break or new line (<br>), end a line with two or more spaces, and then type return.

You can use two or more spaces (commonly referred to as "trailing whitespace") for line breaks in nearly every Markdown application, butt it's controversal. It's hard to see trailing whitespace in an editor, and many people accidentally or intentionally put two spaces after every sentence. For this reason you may want to use something other than trailing whitespace for line beaks.

There two other options: CommonMark and a few other lightweight markup languages let you type a backslash (\) at the end of the line.

## Emphasis

### Bold

To bold text, add two asterisks or underscores before and after a word or phrase. To bold the middle of a word for emphasis, add two asterisks without spaces around the letters.

For example,

Markdown applications don't agree on how to handle undersecores in the middle of a word. For compatibility, use asterisks to bold the middle of a word for emphasis.

```
Love**is**blind
```

### Italic

To italicize text, add one asterisk or underscore before and after a word or phrase. To italicize the middle of a word for emphasis, add one asterisk without spaces around the letters.

For example,

Markdown applications don't agree on how to handle underscores in the middle of a word. For compatibility, use asterisks to italicize the middle of a word for emphasis.

```
A*cat*named dog.
```

### Bold and italic

To emphasize text with bold and italics at the same time, add three asterisks or underscores before and after a word or phrase. To bold and italicize the middle of aword for emphasis, add three asterisks without spaces around the letters.

## Blockquotes

To create a blockquotes, add a > in front of a paragraph.

For example,

```
> I wake in the morning, and I step outside then take a deep breath so I get real high and I scream on top my lungs: "What's going on?"
```

If blockquotes contain multiple paragraphs. Add a > on the blank lines between paragraphs.

Blockquotes can be nested. Add a >> in front of the paragraph you want to nest.

Block quotes can contain other Markdown formatted elements, but not all elements can be used - you'll need to experiment to see which ones work.

## Lists

### Ordered Lists

To create an ordered list, add line items with numbers followed by periods. The numbers don't have to be in numerical order, but the list should start with the number one.

### Unordered Lists

To create an unordered list, add dashes (-), asterisks (*), or plus signs (+) in front of line items. Indent one or more items to create a nested list.

If you need to start an unordered list item with a number followed by a period, you can use a backslash (\) to escape the period.

For compatibility, don't mix and match delimiters in the same list, pick one and stick with it. Indent the element four spaces or one tabb, to add another element in a list while preserving the continuity of the list.

## Code blocks

To represent a code, put it in `.

To represent a code block, put in ```.

## Links

To create a link, enclose the link text in brackets and then follow it immediately with the URL in parentheses.

```
My GitHub is [liemmt28](https://github.com/liemmt28)
```

To quickly turn a URL or email address into a link, enclose it in angle brackets (<,>).

## Image

To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parenthses. You can optionally add a tittle in quotation marks after the parh or URL.

To add a link to an image, enclose the Markdown for the image in brackets, and then add the link in parentheses.
