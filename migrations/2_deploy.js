var HelloWorld = artifacts.require("./HelloWorld.sol");

module.exports = function(deployer) {
    deployer.then(async () => {
        
        var helloWorld = await deployer.deploy(HelloWorld);

        console.log("==== DEPLOYMENT DONE ====")
        console.log("HelloWorld.sol address: " + helloWorld.address);
        console.log("==== DEPLOYMENT DONE ====")
    })
};
