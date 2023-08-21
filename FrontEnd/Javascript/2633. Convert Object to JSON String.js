function jsonStringify(obj) {
    let json = '';
  
    // Check the type of the object
    const type = typeof obj;
  
    // Handle null
    if (obj === null) {
      return 'null';
    }
  
    // Handle strings
    if (type === 'string') {
      return `"${obj}"`;
    }
  
    // Handle numbers and booleans
    if (type === 'number' || type === 'boolean') {
      return obj.toString();
    }
  
    // Handle arrays
    if (Array.isArray(obj)) {
      json += '[';
      for (let i = 0; i < obj.length; i++) {
        json += jsonStringify(obj[i]);
        if (i < obj.length - 1) {
          json += ',';
        }
      }
      json += ']';
      return json;
    }
  
    // Handle objects
    if (type === 'object') {
      json += '{';
      const keys = Object.keys(obj);
      for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const value = jsonStringify(obj[key]);
        json += `"${key}":${value}`;
        if (i < keys.length - 1) {
          json += ',';
        }
      }
      json += '}';
      return json;
    }
  }
  
  // Example usage:
  const obj = {
    name: 'John',
    age: 30,
    city: 'New York',
    married: false,
    children: ['Alice', 'Bob'],
    pets: null
  };
  
  const jsonString = jsonStringify(obj);
  console.log(jsonString);
  // Output: {"name":"John","age":30,"city":"New York","married":false,"children":["Alice","Bob"],"pets":null}
  