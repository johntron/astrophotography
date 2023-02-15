const shortTitle = async page => (await page.title()).replace(/( for Sale)? \| OPT Telescopes/, '');
const shortUrl = original => {
    const url = new URL(original)
    return `${url.pathname}${url.search}`
}

export {shortTitle, shortUrl}
