//npm install --save-dev jest jsdom
// npm install util


const { TextEncoder, TextDecoder } = require('util');
if (typeof global.TextEncoder === 'undefined') {
 global.TextEncoder = TextEncoder;
}
if (typeof global.TextDecoder === 'undefined') {
 global.TextDecoder = TextDecoder;
}
// Importing jsdom to simulate a DOM environment
const { JSDOM } = require('jsdom');
// Mocking the global window and document objects
const { window } = new JSDOM('<!doctype html><html><body></body></html>');
global.document = window.document;
global.window = window;
// Importing the script that contains the functions to test
require('./FakeNews');

// Height Adjustment tests
describe('Textarea dynamic height adjustment', () => {
    test('textarea height adjusts on keyup', () => {
        // Create a textarea element
        const textarea = document.createElement('textarea');
        document.body.appendChild(textarea);
        // Simulate a keyup event
        textarea.dispatchEvent(new KeyboardEvent('keyup', { key: 'a' }));
        // Check if the textarea's height has been adjusted
        expect(textarea.style.height).not.toBe('400px');
    });
});

const {isChecked} = require('./FakeNews');
// Light and Dark mode toggle
describe('Toggle between light and dark modes', () => {
    beforeEach(() => {
        // Create a checkbox and a label for toggling modes
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = 'check';
        document.body.appendChild(checkbox);

        const label = document.createElement('label');
        label.id = 'lightmodetext';
        document.body.appendChild(label);
    });

    // Assuming the setup for JSDOM and global variables is already done

describe('isChecked function', () => {
    it('toggles between light and dark modes', () => {
       // Mock the checkbox and text elements
       const checkbox = document.createElement('input');
       checkbox.type = 'checkbox';
       checkbox.id = 'check';
       document.body.appendChild(checkbox);
   
       const lightModeText = document.createElement('div');
       lightModeText.id = 'lightmodetext';
       document.body.appendChild(lightModeText);
   
       // Initially, the checkbox is unchecked, so the background should be dark
       isChecked();
       expect(document.body.style.background).toBe('linear-gradient(#272727, #181818)');
       expect(lightModeText.textContent).toBe('Dark Mode');
       expect(lightModeText.style.color).toBe('white');
   
       // Check the checkbox to switch to light mode
       checkbox.checked = true;
       isChecked();
       expect(document.body.style.background).toBe('linear-gradient(#e3e3e3, #dcdbdb)');
       expect(lightModeText.textContent).toBe(' Light Mode ');
       expect(lightModeText.style.color).toBe('black');
    });
   });
})   