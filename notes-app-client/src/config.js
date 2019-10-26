export default {
  MAX_ATTACHMENT_SIZE: 5000000,
  s3: {
    REGION: "us-west-2",
    BUCKET: "notes-app-api-dev-attachmentsbucket-1tqgd2rtcuj6p"
  },
  apiGateway: {
    REGION: "us-west-2",
    URL: "https://t0h9zcmqua.execute-api.us-west-2.amazonaws.com/dev"
  },
  cognito: {
    REGION: "us-west-2",
    USER_POOL_ID: "us-west-2_wavxJjtAz",
    APP_CLIENT_ID: "7ollunr377pc5iqd8e78af6o0j",
    IDENTITY_POOL_ID: "us-west-2:7bb0ff19-feca-4d82-afb2-c243c6112e0c"
  }
};
