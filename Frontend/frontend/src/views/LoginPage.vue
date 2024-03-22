<template>
  <div class="Login">
    <Base msg="LIBRARY MANAGEMENT SYSTEM" />

    <form>
      <div class="mb-3">
        <label for="username">Username: </label>
        <input v-model="userName" type="text" placeholder="" />

        <br />

        <label for="password">Password: </label>
        <input v-model="passWord" type="password" placeholder="" />
      </div>
      <div class="mb-2">
        <button class="btn btn-outline-dark" @click="SendLoginRequest">
          Login
        </button>
      </div>
    </form>
  </div>
</template>

<script>
// @ is an alias to /src
import Base from "@/components/Base.vue";

export default {
  name: "BaseComponent",
  components: {
    Base,
  },
  data() {
    return {
      UserDetails: {
        userName: "",
        passWord: "",
      },
    };
  },
  methods: {
    SendLoginRequest() {
      fetch("http://localhost:5000/Login", {
        method: "PUT",
        headers: {
          "Content-Type": "multipart/form-data",
        },
        body: this.UserDetails,
      })
        .then(async (http) => {
          let response = http.text();
          if (http.ok) {
            console.log("created");
            this.$router.push("/home");
          } else {
            return response.then((response) => {
              throw new Error(response);
            });
          }
        })
        .catch((error) => {
          console.log(error);
          console.log(this.UserDetails);
        });
    },
  },
  created() {
    this.SendLoginRequest();
  },
};
</script>

<style scoped>
.mb-3 {
  height: 30px;
  width: 30px;
  align-items: center;
  justify-content: center;
}
.Login {
  display: grid;
  justify-content: center;
  align-items: center;
}
.mb-2 {
  align-items: center;
  justify-content: center;
}
</style>
