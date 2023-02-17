import {describe, expect, it} from "@jest/globals";
import {key} from "./store.mjs";


describe('key', () => {
    it('removes spaces and slashes', () => {
        expect(key(' /')).toBe('__')
    })
    it('should handle', () => {
        expect(key(`/",`)).toBe('')
        expect(key("iOptron CEM40 with iPolar, 1.75-Inch LiteRoc Tripod, and Hard Case")).toBe('iOptron_CEM40_with_iPolar_1.75-Inch_LiteRoc_Tripod_and_Hard_Case')
    })
})