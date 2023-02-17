const key = (str) => str.replaceAll(' ', '_')
    .replaceAll(/[^a-zA-Z0-9!\-_.'()]+/g, '')
    .substring(0, 256)

export {key}
