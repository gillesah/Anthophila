import './polyfills.server.mjs';
import{B as F,H as M,a as x,b as l,c as r,d as f,e as u,f as a,g as p,h as s,i as m,j as v,k as h,l as d,s as g,u as c,v as y,w as b,x as _,y as S}from"./chunk-NMQGPYRI.mjs";var D=(t,e)=>e.id;function w(t,e){if(t&1&&(a(0,"li"),m(1),p()),t&2){let i=e.$implicit;r(),v(i.name)}}function H(t,e){if(t&1&&(a(0,"li"),m(1),p(),a(2,"ul"),m(3),s(4,"br"),m(5," et voici les ruches : "),f(6,w,2,1,"li",null,D),p()),t&2){let i=e.$implicit;r(),v(i.name),r(2),h(" ",i.beekeeper_extended.username," : ",i.beekeeper_extended.public_contact,""),r(3),u(i.beehives_extended)}}var I=(()=>{let e=class e{constructor(){this.data=[],this.httpClient=x(y)}ngOnInit(){this.fetchData()}fetchData(){this.httpClient.get("http://localhost:8002/API_PUBLIC/beeyards/").subscribe(n=>{this.data=n.results,console.log(n)})}};e.\u0275fac=function(o){return new(o||e)},e.\u0275cmp=l({type:e,selectors:[["app-beeyard"]],standalone:!0,features:[d],decls:5,vars:0,template:function(o,C){o&1&&(a(0,"p"),m(1,"beeyard works!"),p(),a(2,"ul"),f(3,H,8,3,null,null,D),p()),o&2&&(r(3),u(C.data))},dependencies:[c,b]});let t=e;return t})();var E=(()=>{let e=class e{constructor(){this.title="front"}};e.\u0275fac=function(o){return new(o||e)},e.\u0275cmp=l({type:e,selectors:[["app-root"]],standalone:!0,features:[d],decls:1,vars:0,template:function(o,C){o&1&&s(0,"app-beeyard")},dependencies:[c,I]});let t=e;return t})();var T=[];var k={providers:[M(T),S()]};var R={providers:[F()]},A=g(k,R);var $=()=>_(E,A),ie=$;export{ie as a};