<template>
  <div>
    첫번째 페이지임
  </div>
</template>

<script>
export default {
  asyncData({
    isDev,
    route,
    store,
    env,
    params,
    query,
    req,
    res,
    redirect,
    error
  }) {
    console.log(res);
  }
};
</script>
