//based on https://github.com/ConsenSys/Tokens/tree/master/test
const TrackParcel = artifacts.require('HelloWorld')


contract('Hello World', async (accounts) => {

    it("set/get message", async () => {
        let instance = await TrackParcel.new();

        await instance.setMessage("Hello World!");

        let result = await instance.message();
        assert.equal(result, "Hello World!");
    })

    it("set/get number", async () => {
        let instance = await TrackParcel.new();

        await instance.setNumber(43);

        let result = await instance.number();
        assert.equal(result.toNumber(), 43);
    })
})