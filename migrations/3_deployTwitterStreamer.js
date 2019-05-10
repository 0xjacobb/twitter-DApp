var TwitterStreamer = artifacts.require("./TwitterStreamer.sol");

module.exports = function(deployer) {
    deployer.then(async () => {
        
        var twitterStreamer = await deployer.deploy(TwitterStreamer);

        console.log("==== DEPLOYMENT DONE ====")
        console.log("TwitterStreamer.sol address: " + twitterStreamer.address);
        console.log("==== DEPLOYMENT DONE ====")
    })
};