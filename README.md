This is a TODO-list web project.

# TDD methodologies
- 编写1个用例-运行测试并按预期失败-编写最少代码实现功能并运行测试直至通过。重复这个步骤，直至没有可写的用例。
- User Story: A description of how the application will work from the point of view of the user. Used to structure a functional test.
- Expected failure: When a test fails in the way that we expected it to.
- TDD and agile software development methodologies often go together, and one of the things we often talk about is the minimum viable app.


# Functional Test == Acceptance Test == End-to-End Test == black box test
- FT(functional test): Tests that use Selenium let us drive a real web browser, so they really let us see how the application functions from the user’s point of view. The main point is that these kinds of tests look at how the whole application functions, from the outside. Another term is black box test, because the test doesn’t know anything about the internals of the system under test. （功能测试是从用户使用角度去验证功能可用。有点类似BDD了）
- FTs should have a human-readable story that we can follow. We make it explicit using comments that accompany the test code. When creating a new FT, we can write the comments first, to capture the key points of the User Story. (在注释中描述功能)
- We’ll see that Django uses them a lot in the files it generates for us to use as a way of suggesting helpful bits of its API. And, of course, we use comments to explain the User Story in our functional tests. (注释的用途。不要去重复代码)

