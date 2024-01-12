const scene = new THREE.Scene();
const geometry=new THREE.BoxGeometry(1, 1, 1);
const material= new THREE.MeshBasicMaterial({color:'blue'});
const  mesh= new THREE.Mesh(geometry, material);
scene.add(mesh);
const sizes={
  width: 600,
  height: 600,
}

// Создаем камеру
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height);
scene.add(camera);

const canvas=document.querySelector('.canvas');
const renderer= new THREE.WebGLRenderer({canvas});
renderer.render(scene, camera);