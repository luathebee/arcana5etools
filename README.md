# arcana5etools
Arcana of the Ancients 5e tools port, I guess

### Left behind:
	*None so far :)

## Instructions

What I'd recommend for helping with the project is:

1. An IDE or Text editor that supports JSON with the following complements/plugins:
	1. JSON Lint - verifies JSON structure, parenthesis and bracket closure
	2. Snippets - for code auto-completion, you press tab and a code section appears "almost perfectly structured", hella usefull for JSON with all of it's curls and  brackets.
	3. Github integration - for pushing, fetching and communicating
2. Arcana of The Ancients PDF
3. 5e.tools - Text Converter
4. 5e.tools - Renderer Demo(for testing/debugging)

### 1. Overview of the Bestiary
#### Meta Section

	{
    "_meta": {
			[... stuff regarding the book...]
		}
  }

#### Creature Data

  "monster": [
		{
			monster1 comes here
		},
		{
			monster2 comes here
		},
		{
			and so on
		}
	}


### 2. Using the Text Converter
Find the section of the creture on the book and paste it as well as possible on the text converter input. Be carefull since the PDF formatting can be really clumsy , selecting things from the next text column, sidebars , etc. Be carefull and check if everything is pasted in order and in the right place.
If the converter didn't ask for manual conversions and everything seems in place, just add it to the code.
##### Fields to avoid/check/be carefull
Take a quick look at Allignment, Armor Types and Traits.
"Language -" - if the language is -, just delete the language line and the converter will fill it correctly.
If things are still breaking, might be needed to check on the Giddy's Github for reference on the statblock.  

### 3. Adding Fluff
At the end of the tags sections, we add the fluff structure. This is for the Info section of the monster and requires most of the manual work. For this, I use the Snippet function on Atom that generates the code structure for this section (there seems to be a Plugin for this in N++) and then we just fill it with the information text.

The structure usually goes like this:

	"fluff":{
		"entries":[
			{
				"type":"entries",
				"entries":[
					"", <------ main info box paragraph
					{
						"type":"entries",
						"name":"",
						"entries":[
							""
						]
					}
				]
			}
		]
	}

#### Other types of fluff entries
"inset", "quote" and "insetReadaloud" are entries that usually pop arround in the bestiary as well, like the dialogs between that elf and dwarf here and there. For this it usually comes in hand to look for reference in the RendererDemo, since everyhting in there is an "entries" type.
Footnotes are also needed for the sidebad information. It can be found at the rendererdemo.

### 4. Uploading and Testing
To check if everything is working properly, upload the Json to the homebrew and check to see if everything is displaying properly.

##### Possible Issues
If the file doesn't even load it's probably a Json structure issue.
If the file shows on the manager, but the section loads forever, it's probably a scheme error with tags, alignment, skills, or entries. Then, it's best to test things on the renderer demo to find the issue.

### 5. Commiting/Pushing to Github.
Working properly, you could commit or push to github and move on to the next spot.

##### Testing 2

So now the we're commiting behind the master, let's see how this works.
